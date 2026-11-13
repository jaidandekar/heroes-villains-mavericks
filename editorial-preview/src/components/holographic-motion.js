(() => {
  const control = document.querySelector('[data-tilt-control]');
  const button = control?.querySelector('button');
  const status = control?.querySelector('[role="status"]');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const coarse = matchMedia('(any-pointer: coarse)');
  if (!control) return;
  const smallScreen = matchMedia('(max-width: 63.99rem)');
  const cards = [...document.querySelectorAll('[data-holo]')];
  const visible = new Set();
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) visible.add(entry.target);
    else { visible.delete(entry.target); reset(entry.target); }
  }));
  cards.forEach(card => observer.observe(card));
  let enabled = false, baseline = null, frame = 0, timer = 0, point = null;
  let permitted = false;
  function reset(card) {
    card.removeAttribute('data-device-tilt');
    ['--holo-rx','--holo-ry','--foil-x','--foil-y','--foil-angle','--foil-hue'].forEach(key => card.style.removeProperty(key));
  }
  function stop(message = '') {
    enabled = false; baseline = null;
    window.removeEventListener('deviceorientation', orient);
    cancelAnimationFrame(frame); frame = 0; clearTimeout(timer);
    cards.forEach(reset);
    button.textContent = 'Enable tilt'; button.setAttribute('aria-pressed','false');
    status.textContent = message || 'Enable tilt to make the foil respond as you move your phone.';
  }
  function orient(event) {
    if (!enabled || document.hidden || reduced.matches || !Number.isFinite(event.beta) || !Number.isFinite(event.gamma)) return;
    clearTimeout(timer); status.textContent = '';
    if (!baseline) baseline = { beta: event.beta, gamma: event.gamma };
    const wrap = value => ((value + 540) % 360) - 180;
    const beta = wrap(event.beta - baseline.beta);
    const gamma = wrap(event.gamma - baseline.gamma);
    const angle = (screen.orientation?.angle ?? window.orientation ?? 0) * Math.PI / 180;
    const clamp = value => Math.max(-1,Math.min(1,value / 12));
    point = { x: clamp(gamma * Math.cos(angle) + beta * Math.sin(angle)), y: clamp(beta * Math.cos(angle) - gamma * Math.sin(angle)) };
    if (frame) return;
    frame = requestAnimationFrame(() => {
      frame = 0;
      visible.forEach(card => {
        card.style.setProperty('--holo-rx',(-point.y * 5).toFixed(2) + 'deg');
        card.style.setProperty('--holo-ry',(point.x * 6.5).toFixed(2) + 'deg');
        card.style.setProperty('--foil-x',(50 + point.x * 50).toFixed(1) + '%');
        card.style.setProperty('--foil-y',(50 + point.y * 50).toFixed(1) + '%');
        card.style.setProperty('--foil-angle',(115 + point.x * 25 + point.y * 10).toFixed(1) + 'deg');
        card.style.setProperty('--foil-hue',(point.x * 18).toFixed(1) + 'deg');
        card.setAttribute('data-device-tilt','');
      });
    });
  }
  function availability() {
    const phone = coarse.matches || smallScreen.matches;
    control.hidden = !phone;
    button.disabled = false;
    if (!phone) { stop(); return; }
    if (reduced.matches) {
      stop('Tilt is off because Reduce Motion is enabled on your device.');
      button.disabled = true;
    } else if (!window.isSecureContext || !window.DeviceOrientationEvent) {
      stop('Motion access is unavailable in this browser; try opening this page in Safari.');
      button.disabled = true;
    } else if (!enabled) {
      status.textContent = 'Enable tilt to make the foil respond as you move your phone.';
    }
  }
  button.addEventListener('click', async () => {
    if (enabled) { stop(); return; }
    button.disabled = true;
    try {
      const api = window.DeviceOrientationEvent;
      if (!permitted && typeof api.requestPermission === 'function' && await api.requestPermission() !== 'granted') {
        status.textContent = 'Motion access was not enabled. The foil still works without it.';
        return;
      }
      if (reduced.matches || document.hidden) return;
      permitted = true;
      enabled = true; baseline = null;
      button.textContent = 'Disable tilt'; button.setAttribute('aria-pressed','true');
      status.textContent = 'Tilt your device to move the foil.';
      window.addEventListener('deviceorientation',orient,{passive:true});
      timer = setTimeout(() => stop('No motion sensor data received. You can try again.'),6000);
    } catch {
      stop('Motion access is unavailable. The foil still works without it.');
    } finally { button.disabled = false; }
  });
  document.addEventListener('visibilitychange',() => {
    if (!enabled) return;
    baseline = null; cards.forEach(reset);
    if (document.hidden) { cancelAnimationFrame(frame); frame = 0; clearTimeout(timer); }
  });
  window.addEventListener('orientationchange',() => { baseline = null; cards.forEach(reset); });
  screen.orientation?.addEventListener?.('change',() => { baseline = null; cards.forEach(reset); });
  reduced.addEventListener('change',availability);
  coarse.addEventListener('change',availability);
  smallScreen.addEventListener('change',availability);
  availability();
})();
