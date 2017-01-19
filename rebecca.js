/**
 * Created by rebeccaemmerich on 1/18/17.
 */

var object = {
    tag: "img",
    src: "http://www.blueskycommunityhealingcentre.ca/wp-content/themes/risen/images/backgrounds/sun.jpg"
}
var title = {
    tag: "h1",
    innerHTML: "HELLO"
}
var nav = {
    func: "navbar",
    tag: "ul",
    src: "",
    innerHTML: ["Home", "News", "About", "Contact Us"]
}

function insertImage() {
    var element = document.createElement(object.tag);
    element.setAttribute("src", object.src);
    element.setAttribute("width", "300px");
    element.setAttribute("height", "220px");
    document.body.appendChild(element);

}

insertImage();

function words() {
    var element = document.createElement(title.tag);
    var object2 = document.createTextNode(title.innerHTML);
    document.body.appendChild(element);
    element.appendChild(object2);
}

words();


function navbar(){
    var list = document.createElement('UL');
    var ul = document.createElement('UL');
    var ul2 = document.createElement('UL');
    var ul3 = document.createElement('UL');
    var ul4 = document.createElement('UL')
    var object2 = document.createTextNode(nav.innerHTML[0]);
    var object3 = document.createTextNode(nav.innerHTML[1]);
    var object4 = document.createTextNode(nav.innerHTML[2]);
    var object5 = document.createTextNode(nav.innerHTML[3]);
    ul.style.display= "inline-block";
    ul2.style.display= "inline-block";
    ul3.style.display= "inline-block";
    ul4.style.display ="inline-block";
    list.style.backgroundColor = "lightcyan";
    list.style.paddingTop = "15px";
    list.style.paddingBottom = "15px";
    list.style.fontFamily = "arial";

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

navbar();

