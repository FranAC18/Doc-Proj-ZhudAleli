// Ejecutar con Node y PLAYWRIGHT_MODULE apuntando al paquete Playwright disponible.
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const resultados = [];
const errores = [];

async function mostrarError(pagina) {
  await pagina.goto('http://127.0.0.1:8000/acceso/');
  await pagina.locator('button[type="submit"]').click();
  await pagina.locator('[data-notificacion]').waitFor();
}

async function medir(pagina) {
  return pagina.evaluate(() => {
    const aviso = document.querySelector('[data-notificacion]');
    const dialogo = document.querySelector('[data-notificacion-dialog]');
    const caja = aviso.getBoundingClientRect();
    return {
      x: caja.x, y: caja.y, ancho: caja.width, alto: caja.height,
      oculto: aviso.hidden,
      opacidad: Number(getComputedStyle(aviso).opacity),
      radio: getComputedStyle(aviso).borderRadius,
      radioCampo: getComputedStyle(document.querySelector('input[name="username"]')).borderRadius,
      desbordePagina: document.documentElement.scrollWidth > innerWidth,
      barraHorizontal: getComputedStyle(dialogo).overflowX,
      scrollHorizontal: dialogo.scrollLeft,
      modal: dialogo.getAttribute('aria-modal'),
      fondoInerte: document.querySelector('.za-app-shell').inert,
      foco: document.activeElement.id || document.activeElement.tagName,
    };
  });
}

async function muestrearAnimacion(pagina, nombre, tiempos) {
  return pagina.evaluate(({ nombre, tiempos }) => {
    const aviso = document.querySelector('[data-notificacion]');
    const animacion = aviso.getAnimations().find((item) => item.animationName === nombre);
    if (!animacion) throw new Error(`No se encontró ${nombre}`);
    animacion.pause();
    return tiempos.map((tiempo) => {
      animacion.currentTime = tiempo;
      const caja = aviso.getBoundingClientRect();
      const dialogo = document.querySelector('[data-notificacion-dialog]');
      return {
        tiempo, x: caja.x, y: caja.y, opacidad: Number(getComputedStyle(aviso).opacity),
        oculto: aviso.hidden,
        desbordePagina: document.documentElement.scrollWidth > innerWidth,
        barraHorizontal: getComputedStyle(dialogo).overflowX,
        scrollHorizontal: dialogo.scrollLeft,
      };
    });
  }, { nombre, tiempos });
}

(async () => {
  const navegador = await chromium.launch({ channel: 'msedge', headless: true });
  try {
    for (const ancho of [360, 375, 768, 1280, 1440]) {
      const pagina = await navegador.newPage({ viewport: { width: ancho, height: 900 } });
      // El muestreo manual y las capturas no deben competir con los temporizadores reales.
      // El autocierre y las pausas se comprueban aparte sin esta instrumentación.
      await pagina.addInitScript(() => {
        const programar = window.setTimeout.bind(window);
        window.setTimeout = (accion, demora, ...argumentos) => programar(
          accion, demora === 3000 || demora === 720 ? 60000 : demora, ...argumentos
        );
      });
      pagina.on('pageerror', (error) => errores.push(String(error)));
      pagina.on('response', (respuesta) => {
        if (respuesta.status() >= 400) errores.push(`${respuesta.status()} ${respuesta.url()}`);
      });
      await mostrarError(pagina);
      const entrada = await muestrearAnimacion(pagina, 'za-modal-entrada', [0, 160, 320, 480, 639]);
      const movil = ancho < 768;
      const eje = movil ? 'y' : 'x';
      const ejeFijo = movil ? 'x' : 'y';
      assert(entrada.every((muestra, indice) => !indice || (movil
        ? muestra.y > entrada[indice - 1].y
        : muestra.x < entrada[indice - 1].x)));
      assert(entrada.every((muestra) => muestra[ejeFijo] === entrada[0][ejeFijo]));
      const visible = await medir(pagina);
      assert.equal(visible.radio, visible.radioCampo);
      assert.equal(visible.modal, 'true');
      assert.equal(visible.fondoInerte, true);
      await pagina.screenshot({ path: path.join(__dirname, `direcciones-visible-${ancho}.png`) });
      await pagina.keyboard.press('Tab');
      assert(await pagina.locator('[data-notificacion-dialog]').evaluate((dialogo) => dialogo.contains(document.activeElement)));
      await pagina.keyboard.press('Escape');
      const salida = await muestrearAnimacion(pagina, 'za-modal-salida', [0, 160, 320, 480, 600]);
      assert(salida.every((muestra, indice) => !indice || (movil
        ? muestra.y < salida[indice - 1].y
        : muestra.x > salida[indice - 1].x)));
      assert(salida.every((muestra) => !muestra.oculto && muestra[ejeFijo] === salida[0][ejeFijo]));
      assert(Math.abs(salida[2][eje] - visible[eje]) > 100);
      await pagina.evaluate(() => {
        document.querySelector('[data-notificacion]').getAnimations()[0].currentTime = 320;
      });
      await pagina.screenshot({ path: path.join(__dirname, `direcciones-salida-${ancho}.png`) });
      await pagina.evaluate(() => document.querySelector('[data-notificacion]').getAnimations()[0]?.play());
      await pagina.locator('[data-notificacion]').waitFor({ state: 'hidden' });
      const cerrado = await medir(pagina);
      assert.equal(cerrado.modal, null);
      assert.equal(cerrado.fondoInerte, false);
      assert.equal(cerrado.foco, 'id_username');
      await pagina.keyboard.press('Tab');
      assert.equal(await pagina.locator('input[name="password"]').evaluate((campo) => campo === document.activeElement), true);
      await pagina.keyboard.press('Escape');
      assert.equal((await medir(pagina)).fondoInerte, false);
      assert([...entrada, ...salida, visible, cerrado].every((muestra) => !muestra.desbordePagina && muestra.barraHorizontal === 'hidden' && muestra.scrollHorizontal === 0));
      resultados.push({ ancho, entrada, visible, salida, cerrado });
      await pagina.close();
    }

    const pagina = await navegador.newPage({ viewport: { width: 1280, height: 900 } });
    await mostrarError(pagina);
    await pagina.locator('[data-notificacion]').hover();
    await pagina.waitForTimeout(3300);
    assert.equal((await medir(pagina)).oculto, false);
    await pagina.mouse.move(20, 800);
    await pagina.locator('[data-notificacion]').waitFor({ state: 'hidden', timeout: 4500 });
    resultados.push({ caso: 'pausa-hover-y-autocierre', correcto: true });

    await mostrarError(pagina);
    await pagina.waitForTimeout(700);
    await pagina.locator('[data-cerrar-notificacion]').click();
    await pagina.locator('[data-notificacion]').waitFor({ state: 'hidden' });
    assert.equal((await medir(pagina)).fondoInerte, false);
    resultados.push({ caso: 'cierre-boton', correcto: true });

    await mostrarError(pagina);
    await pagina.waitForTimeout(700);
    await pagina.locator('[data-campo-error]').last().click();
    await pagina.locator('[data-notificacion]').waitFor({ state: 'hidden' });
    assert.equal((await medir(pagina)).foco, 'id_password');
    resultados.push({ caso: 'enlace-al-campo', correcto: true });

    await mostrarError(pagina);
    await pagina.evaluate(() => {
      const aviso = document.querySelector('[data-notificacion]');
      const animacion = aviso.getAnimations()[0];
      animacion.pause();
      animacion.currentTime = 100;
    });
    const antesDeCerrar = await medir(pagina);
    await pagina.keyboard.press('Escape');
    const cierreAnticipado = await muestrearAnimacion(pagina, 'za-modal-salida', [0]);
    assert(Math.abs(antesDeCerrar.x - cierreAnticipado[0].x) < 1);
    await pagina.locator('[data-notificacion]').waitFor({ state: 'hidden' });
    resultados.push({ caso: 'cierre-durante-entrada-sin-salto', correcto: true });

    await pagina.setViewportSize({ width: 720, height: 450 });
    await mostrarError(pagina);
    await pagina.waitForTimeout(700);
    await pagina.evaluate(() => {
      const lista = document.querySelector('.za-error-list');
      for (let indice = 0; indice < 18; indice += 1) {
        const item = document.createElement('li');
        item.textContent = `Error de prueba ${indice}: ${'TextoLargoSinEspacios'.repeat(12)}`;
        lista.append(item);
      }
    });
    const textoLargo = await medir(pagina);
    assert.equal(textoLargo.desbordePagina, false);
    assert.equal(textoLargo.barraHorizontal, 'hidden');
    await pagina.locator('[data-cerrar-notificacion]').focus();
    await pagina.waitForTimeout(3200);
    assert.equal((await medir(pagina)).oculto, false);
    const desplazamiento = await pagina.locator('[data-notificacion-dialog]').evaluate((dialogo) => {
      dialogo.scrollTop = dialogo.scrollHeight;
      return dialogo.scrollTop;
    });
    assert(desplazamiento > 0);
    await pagina.keyboard.press('Escape');
    await pagina.locator('[data-notificacion]').waitFor({ state: 'hidden' });
    resultados.push({ caso: 'reflujo-200-texto-largo-pausa-foco', correcto: true, desplazamiento });

    await pagina.emulateMedia({ reducedMotion: 'reduce' });
    await mostrarError(pagina);
    const movimientoReducido = await pagina.locator('[data-notificacion]').evaluate((aviso) => ({
      nombre: getComputedStyle(aviso).animationName,
      duracion: getComputedStyle(aviso).animationDuration,
      transformacion: getComputedStyle(aviso).transform,
    }));
    assert.equal(movimientoReducido.nombre, 'za-modal-fade-entrada');
    assert.equal(movimientoReducido.transformacion, 'none');
    await pagina.keyboard.press('Escape');
    await pagina.locator('[data-notificacion]').waitFor({ state: 'hidden' });
    resultados.push({ caso: 'movimiento-reducido', ...movimientoReducido });
    await pagina.close();

    assert.deepEqual(errores, []);
    fs.writeFileSync(path.join(__dirname, 'direcciones-verificacion.json'), JSON.stringify({ resultados, errores }, null, 2));
    console.log(`${resultados.length} escenarios correctos; sin desbordamiento ni errores de recursos o JavaScript.`);
  } finally {
    await navegador.close();
  }
})().catch((error) => { console.error(error); process.exitCode = 1; });
