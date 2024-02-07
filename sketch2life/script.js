const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');
const rect = canvas.getBoundingClientRect();

canvas.width = 1000;  
canvas.height = 512;  

let isDrawing = false;
let drawMode = true; // true for drawing, false for erasing

canvas.addEventListener('mousedown', function(e) {
    isDrawing = true;
    draw(e);
});

canvas.addEventListener('mouseup', function() {
    isDrawing = false;
    ctx.beginPath();
});

canvas.addEventListener('mousemove', draw);

function setDraw() {
    drawMode = true;
    ctx.globalCompositeOperation = "source-over";
}

function setErase() {
    drawMode = false;
    ctx.globalCompositeOperation = "destination-out";
}

function draw(e) {
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    if (!isDrawing) return;

    ctx.lineWidth = drawMode ? 5 : 20; // thicker line for eraser
    ctx.lineCap = 'round';
    ctx.strokeStyle = drawMode ? 'black' : 'white'; // white color for eraser

    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
}



async function processSketch() {
    console.log('Starting to process the sketch.'); // Logging statement
    
    // Show spinner and progress bar
    document.getElementById('spinner').style.display = 'inline-block';
    document.getElementById('progressBar').style.display = 'block';
    
    // Convert canvas to dataURL
    const dataURL = canvas.toDataURL('image/png');
    
    console.log('Canvas converted to dataURL.'); // Logging statement

    try {
        console.log('Attempting to send POST request to /predict.'); // Logging statement
        
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: dataURL }),
        });
        
        if (!response.ok) {
            console.log(`Received an unsuccessful status code: ${response.status}`); // Logging statement
            throw new Error('Network response was not ok');
        }
        
        console.log('Successfully received a response from the server.'); // Logging statement

        const blob = await response.blob();
        
        // Hide spinner and update progress bar
        document.getElementById('spinner').style.display = 'none';
        document.getElementById('progressBar').style.width = '100%';
        
        console.log('Response processed and image displayed.'); // Logging statement

        document.getElementById('outputImage').src = URL.createObjectURL(blob);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        if(error.response) {
            console.error('Response Error:', error.response);
        }
        alert("An error occurred while processing the sketch. Please try again.");
    } finally {
        console.log('Fetch operation completed. Resetting UI elements.'); // Logging statement
        
        // Reset progress bar and spinner
        document.getElementById('spinner').style.display = 'none';
        document.getElementById('progressBar').style.width = '0%';
    }    
}

