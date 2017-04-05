function backcolor_right() {
    var x = $(".right-part").css("height");
    $(".left-part").css("height",x);
};

function backcolor_left() {
    var x = $(".left-part").css("height");
    $(".right-part").css("height",x);
};

$(document).ready(function(){
    
    right = $(".right-part").css("height").split('');
    right.splice((right.length-2),2);
    right = right.join('');

    left = $(".left-part").css("height").split('');
    left.splice((left.length-2),2);
    left = left.join('');
    
    if (+right > +left) {
        backcolor_right();
    } else {
        backcolor_left();           
    };
    
});
