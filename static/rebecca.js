// /**
//  * Created by rebeccaemmerich on 1/18/17.
//  */


// var object = {
//     type: "images",
//     tag: "img",
//     src: "http://www.blueskycommunityhealingcentre.ca/wp-content/themes/risen/images/backgrounds/sun.jpg"
//  }
// var object = {
//     type: "words",
//     tag: "p",
//     size: "small",
//     innerHTML: "HELLO"
//  }
// var object = {
//     type: "words",
//     tag: "BUTTON",
//     innerHTML: "CLICK ME"
//  }
// var object = {
//     type: "navbar",
//     tag: "ul",
//     src: "",
//     color: "green"
// }
// var json_object = {
//     type: "vid",
//     tag: "iframe",
//     src: "https://www.youtube.com/embed/4Ru2eei4NQk"
// }


function getFrontendElement(json_object){
    if(json_object.type === "image"){
        insertImage(json_object);
    }
    else if(json_object.type === "title"){
        insertTitle(json_object)
    }
    else if(json_object.type === "navbar"){
        insertNavbar(json_object)
    }
    else if(json_object.type === "video"){
        insertVideo(json_object);
    }
    else if(json_object.type === "button"){
        insertButton(json_object)
    }
    else if(json_object.type === "paragraph"){
        insertParagraph(json_object)
    }
    else if(json_object.type === "link"){
        insertLink(json_object)
    }
}


function insertImage(object) {
    var element = document.createElement(object.tag);
    element.setAttribute("src", object.src);
    element.setAttribute("width", "300px");
    element.setAttribute("align", "center");
    var preview = document.getElementById('preview');
    preview.appendChild(element);

}

function insertVideo(object) {
    var element = document.createElement(object.tag);
    element.setAttribute("src", object.src);
    element.setAttribute("width", "500px");
    element.setAttribute("height", "350px");
    element.setAttribute("align", "center");
    var preview = document.getElementById('preview');
    preview.appendChild(element);
}



function insertTitle(object) {
    var element = document.createElement("h1");
    var object2 = document.createTextNode(object.innerHTML);
    element.style.fontFamily = "arial";
    element.style.textAlign = "center";
    element.style.fontSize = object.size;
    var preview = document.getElementById('preview');
    preview.appendChild(element);
    element.appendChild(object2);
}

function insertLink(object) {
    var element = document.createElement("a");
    var object2 = document.createTextNode(object.href);
    element.style.fontFamily = "arial";
    element.style.textAlign = "center";
    element.style.fontSize = object.size;
    element.setAttribute("href", object.href);
    var preview = document.getElementById('preview');
    preview.appendChild(element);
    element.appendChild(object2);
}



function insertParagraph(object) {
    var element = document.createElement("p");
    var object2 = document.createTextNode(object.innerHTML);
    element.style.fontFamily = "arial";
    element.style.textAlign = "center";
    element.style.fontSize = object.size;
    var preview = document.getElementById('preview');
    preview.appendChild(element);
    element.appendChild(object2);
}


function insertButton(object) {
    var element = document.createElement("BUTTON");
    var object2 = document.createTextNode(object.innerHTML);
    element.style.fontFamily = "arial";
    element.style.textAlign = "center";
    element.style.fontSize = object.size;
    var preview = document.getElementById('preview');
    preview.appendChild(element);
    element.appendChild(object2);
}



function insertNavbar(object){
    var list = document.createElement('UL');
    var ul = document.createElement('UL');
    var ul2 = document.createElement('UL');
    var ul3 = document.createElement('UL');
    var ul4 = document.createElement('UL')
    var object2 = document.createTextNode("Info");
    var object3 = document.createTextNode("About us");
    var object4 = document.createTextNode("News");
    var object5 = document.createTextNode("Contact us");
    ul.style.display= "inline-block";
    ul2.style.display= "inline-block";
    ul3.style.display= "inline-block";
    ul4.style.display ="inline-block";
    list.style.backgroundColor = object.color;
    list.style.paddingTop = "15px";
    list.style.paddingBottom = "15px";
    list.style.fontFamily = "arial";
    list.style.textAlign = "right";

    var preview = document.getElementById('preview');
    preview.appendChild(list);
    list.appendChild(ul);
    list.appendChild(ul2);
    list.appendChild(ul3);
    list.appendChild(ul4);
    ul.appendChild(object2);
    ul2.appendChild(object3);
    ul3.appendChild(object4);
    ul4.appendChild(object5);
}



