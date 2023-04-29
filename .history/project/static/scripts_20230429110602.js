// Get the necessary elements
const fileInput = document.getElementById('file-input');
const dragDropBox = document.getElementById('drag-drop-box');
const resultPopup = document.getElementById('result-popup');
const resultImage = document.getElementById('result-image');
const learnMoreButton = document.getElementById('learn-more-button');
const resultsSection = document.getElementById('results-section');

// Add event listeners
fileInput.addEventListener('change', handleFileSelect);
dragDropBox.addEventListener('dragenter', handleDragEnter);
dragDropBox.addEventListener('dragleave', handleDragLeave);
dragDropBox.addEventListener('dragover', handleDragOver);
dragDropBox.addEventListener('drop', handleFileSelect);
learnMoreButton.addEventListener('click', scrollToResults);

// Handle file selection
function handleFileSelect(event) {
  event.preventDefault();
  const file = event.target.files[0];
  if (file) {
    displayImage(file);
  }
}

// Display the image in the drag and drop box
function displayImage(file) {
  dragDropBox.classList.add('hidden');
  resultImage.src = URL.createObjectURL(file);
  resultPopup.classList.remove('hidden');
}

// Handle drag enter
function handleDragEnter(event) {
  event.preventDefault();
  dragDropBox.classList.add('drag-over');
}

// Handle drag leave
function handleDragLeave(event) {
  event.preventDefault();
  dragDropBox.classList.remove('drag-over');
}

// Handle drag over
function handleDragOver(event) {
  event.preventDefault();
}

// Scroll to results section
function scrollToResults() {
  resultsSection.scrollIntoView({ behavior: 'smooth' });
}
