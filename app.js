var express = require("express"),
    app = express(),
    body = require("body-parser"),
    multer = require("multer"),
    ejs= require("ejs");


app.set("view engine","ejs");

app.use(express.static("./public"));

app.get("/",function(req,res){
    res.render("index");
});


app.listen(3000,function(){
    console.log("Server started at 3000");
});