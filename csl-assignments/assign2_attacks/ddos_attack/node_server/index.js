const express = require("express");

const port = 8080;

const app = express();
app.get("/welcome", (req, res) => {
  res.status(200).end();
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
