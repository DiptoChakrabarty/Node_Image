var express = require("express"),
    app = express(),
    body = require("body-parser"),
    multer = require("multer"),
    ejs= require("ejs"),
    path= require("path");
    let {pyshell}= require("python-shell"),
    global=require("global");

//Set Storage Engine

var spawn = require("child_process").spawn;

var storage= multer.diskStorage({
    destination: "./public/uploads",
    filename: function(req,file,cb){
        cb(null,file.filename + '-' + Date.now() +
        path.extname(file.originalname));
    }
});

// Setup Upload
var upload = multer({
    storage: storage,
    limits: {fileSize: 100000},
    fileFilter: function(req,file,cb){
        checkfiletype(file,cb);
    }
}).single('upload[file]');


//Check FileType Function
function checkfiletype(file,cb){
    var filetypes = /jpeg|jpg|png|gif/;
    //check file extension
    var extname= filetypes.test(path.extname(file.originalname).toLowerCase());
    // check mime
    var mimetype = filetypes.test(file.mimetype);

    if(mimetype && extname){
        return cb(null,true);
    } else {
        cb("Error Images Only");
    }
}
function callD_alembert(path) {
    
    console.log(path);
    var Process = spawn("python3",["./imagecluster.py",path]);
    };


app.set("view engine","ejs");

app.use(express.static("./public"));

app.get("/",function(req,res){
    res.render("index");
});


app.post("/upload",function(req,res){
    upload(req,res,(err)=>{
        if(err){
            res.send("/Not Found");
        }else{
            console.log(req.file);
            var path= "./" + req.file.path;

            console.log(path);
           // var Process = spawn("python3",["./imagecluster.py",path]);
           callD_alembert(path);
            res.redirect("/");
        }
    });
});

app.get("/newimage",callD_alembert);


  


app.listen(3000,function(){
    console.log("Server started at 3000");
});