const vbWidthSlider = document.getElementById('vbWidth');
const vbHeightSlider = document.getElementById('vbHeight');
const vbWidthValue = document.getElementById('vbWidthValue');
const vbHeightValue = document.getElementById('vbHeightValue');
const demoSVG = document.getElementById('demoSVG');
const zoomPercent = document.getElementById('zoomPercent');
const resetBtn = document.getElementById('resetBtn');

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

function resetViewBox() {
  vbWidthSlider.value = baselineWidth;
  vbHeightSlider.value = baselineHeight;
  updateViewBox();
}

vbWidthSlider.addEventListener('input', updateViewBox);
vbHeightSlider.addEventListener('input', updateViewBox);
resetBtn.addEventListener('click', resetViewBox);

// Initialize
updateViewBox();
