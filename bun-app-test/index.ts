import express from "express";

const app = express();

app.get("/", (req, res) => {
  res.send({
    name: "Vansh",
    email: "vansh@gmail.com",
    username: "vansh2744",
  });
});

app.listen(8000, () => {
  console.log("App running on host : 8000");
});
