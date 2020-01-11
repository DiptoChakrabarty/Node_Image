var express = require("express"),
    app = express(),
    body = require("body-parser"),
    multer = require("multer"),
    ejs= require("ejs"),
    path= require("path");

//Set Storage Engine

var storage= multer.diskStorage({
    destination: "./public/uploads",
    filename: function(req,file,cb){
        cb(null,file.filename + '-' + Date.now() +
        path.extname(file.originalname));
    }
});

// Setup Upload
var upload = multer({
    storage: storage
}).single('upload[file]');


app.set("view engine","ejs");

app.use(express.static("./public"));

app.get("/",function(req,res){
    res.render("index");
});


app.post("/upload",function(req,res){
    upload(req,res,(err)=>{
        if(err){
            res.redirect("/");
        }else{
            console.log(req.file);
            res.redirect("/");
        }
    });
});


app.listen(3000,function(){
    console.log("Server started at 3000");
});