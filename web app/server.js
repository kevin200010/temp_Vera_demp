const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const { exec } = require('child_process');
const findFreePort = require('./findFreePort');

const app = express();

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const dir = './public/uploads';
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    cb(null, dir);
  },
  filename: (req, file, cb) => {
    cb(null, 'uploaded_audio.wav');
  }
});

const upload = multer({ storage: storage });

app.use(express.static(path.join(__dirname, 'public')));

// New route to handle audio conversion
app.post('/convert', upload.single('audio'), (req, res) => {
  const inputFilePath = path.join(__dirname, 'public/uploads/uploaded_audio.wav');
  const outputFilePath = path.join(__dirname, 'public/uploads/converted_audio.wav');

  
  // Use FFmpeg to convert audio format if needed
  const ffmpegCommand = `ffmpeg -i  "C:\\Users\\kevin\\OneDrive\\Documents\\VERN.ai\\Cobalt\\End Point for VERA\\new deliverable\\deliverable-20240604\\web app\\public\\uploads\\uploaded_audio.wav" -acodec pcm_s16le -ar 16000 -ac 1 "C:\\Users\\kevin\\OneDrive\\Documents\\VERN.ai\\Cobalt\\End Point for VERA\\new deliverable\\deliverable-20240604\\web app\\public\\uploads\\converted_audio.wav"`;
  
  exec(ffmpegCommand, (error, stdout, stderr) => {
    if (error) {
      console.error(`FFmpeg error: ${error}`);
      res.status(500).send('Audio conversion failed');
      return;
    }
    console.log('Audio conversion successful');
    // res.sendFile(outputFilePath);
  });


    // Define the command to execute the Python client script
    const pythonCommand = `python  "C:\\Users\\kevin\\OneDrive\\Documents\\VERN.ai\\Cobalt\\End Point for VERA\\new deliverable\\deliverable-20240604\\python-client\\client.py"`;

    // Execute the command
    exec(pythonCommand, (error, stdout, stderr) => {
    if (error) {
        console.error(`Python script error: ${error}`);
        console.error(`Python script stderr: ${stderr}`);
        res.status(500).send('Error executing Python script');
        return;
    }
    console.log('Python script output:', stdout);
    // Process the output as needed
    // Send the Python script output as the response
    res.status(200).send(stdout);
});


});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

findFreePort(3000, (err, port) => {
  if (err) {
    console.error('Error finding a free port:', err);
    return;
  }

  app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
  });
});
