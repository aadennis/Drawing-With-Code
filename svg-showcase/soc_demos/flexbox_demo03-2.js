const vbWidthSlider = document.getElementById('vbWidth');
const vbHeightSlider = document.getElementById('vbHeight');
const vbWidthValue = document.getElementById('vbWidthValue');
const vbHeightValue = document.getElementById('vbHeightValue');
const demoSVG = document.getElementById('demoSVG');
const zoomPercent = document.getElementById('zoomPercent');
const resetBtn = document.getElementById('resetBtn');

const zoomSlider = document.getElementById('zoomSlider');
const zoomSliderValue = document.getElementById('zoomSliderValue');

const baselineWidth = 240;
const baselineHeight = 280;

function updateViewBox() {
  const w = parseInt(vbWidthSlider.value, 10);
  const h = parseInt(vbHeightSlider.value, 10);
  vbWidthValue.textContent = w;
  vbHeightValue.textContent = h;
  demoSVG.setAttribute('viewBox', `0 0 ${w} ${h}`);

  // Calculate zoom percentage relative to baseline
  const zoomW = baselineWidth / w;
  const zoomH = baselineHeight / h;
  const zoom = ((zoomW + zoomH) / 2) * 100;
  zoomPercent.textContent = zoom.toFixed(0) + "%";
}

function updateUniformZoom() {
  const zoomValue = parseInt(zoomSlider.value, 10);
  zoomSliderValue.textContent = zoomValue + "%";

  // Scale width and height uniformly
  const w = Math.round(baselineWidth * (100 / zoomValue));
  const h = Math.round(baselineHeight * (100 / zoomValue));

  vbWidthSlider.value = w;
  vbHeightSlider.value = h;
  updateViewBox();
}

function resetViewBox() {
  vbWidthSlider.value = baselineWidth;
  vbHeightSlider.value = baselineHeight;
  zoomSlider.value = 100;
  zoomSliderValue.textContent = "100%";
  updateViewBox();
}

vbWidthSlider.addEventListener('input', updateViewBox);
vbHeightSlider.addEventListener('input', updateViewBox);
zoomSlider.addEventListener('input', updateUniformZoom);
resetBtn.addEventListener('click', resetViewBox);

// Initialize
updateViewBox();