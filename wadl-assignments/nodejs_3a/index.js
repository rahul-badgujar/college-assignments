const express = require('express');
const app = express();
const port = 4000;

//to make pages .html .txt .jpeg .mp3 .mp4  static content 
app.use(express.static("public"));

app.listen(port, () => {
    console.log(`app started on port ${port}`);
})