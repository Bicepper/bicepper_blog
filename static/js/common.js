$(function(){
    var current_color = "";

    $(".button").hover(
        function(){
            var classlist = $(this).attr("class").split(" ");
            for(var i=0; i<classlist.length; i++){
                if(classlist[i].indexOf("button-color") >= 0){
                    current_color = classlist[i].split("-")[2];
                    console.log(current_color);
                    $(this).removeClass("button-color-" + current_color);
                    $(this).addClass("button-color-" + current_color + "-on");
                }
            }
        },
        function(){
            $(this).removeClass("button-color-" + current_color + "-on");
            $(this).addClass("button-color-" + current_color);
        }
    );

    var scrollButton = $('.scroll-top');
    // scrollButton.hide();
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            scrollButton.fadeIn("fast");
        } else {
            scrollButton.fadeOut("fast");
        }
    });
    //スクロールしてトップ
    scrollButton.click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 500);
        return false;
    });
});