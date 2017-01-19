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
// var object = {
//     type: "vid",
//     tag: "iframe",
//     src: "https://www.youtube.com/embed/4Ru2eei4NQk"
// }

function getFrontendElement(object){
    if(object.type === "image"){
        insertImage()
    }
    else if(object.type === "words"){
        words()
    }
    else if(object.type === "navbar"){
        navbar()
    }
    else if(object.type === "video"){
        insertVideo(object);
    }
    else if(object.type === "images"){
        insertImage()
    }
}

// chooseFunction()

function insertImage() {
    var element = document.createElement(object.tag);
    element.setAttribute("src", object.src);
    element.setAttribute("width", "300px");
    element.setAttribute("height", "220px");
    document.body.appendChild(element);

}

function insertVideo(object) {
    var element = document.createElement(object.tag);
    element.setAttribute("src", object.src);
    element.setAttribute("width", "300px");
    element.setAttribute("height", "220px");
    // document.body.appendChild(element);
    return element
}



function words() {
    var element = document.createElement(object.tag);
    var object2 = document.createTextNode(object.innerHTML);
    element.style.fontFamily = "arial";
    element.style.textAlign = "center";
    element.style.fontSize = object.size;
    document.body.appendChild(element);
    element.appendChild(object2);
}



function navbar(){
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

    document.body.appendChild(list);
    list.appendChild(ul);
    list.appendChild(ul2);
    list.appendChild(ul3);
    list.appendChild(ul4);
    ul.appendChild(object2);
    ul2.appendChild(object3);
    ul3.appendChild(object4);
    ul4.appendChild(object5);
}



