var express = require("express"),
    app = express(),
    body = require("body-parser"),
    multer = require("multer");

app.get("/",function(req,res){
    res.send("Initial Page");
});


app.listen(3000,function(){
    console.log("Server started at 3000");
});