$(document).ready(function(){
    $('.main-slide').slick({
        lazyLoad: 'progressive',
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade:true,
        asNavFor: '.slider-nav'
    })
    $('.slider-nav').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        asNavFor: '.main-slide',
        focusOnSelect: true,
        responsive: [
            {
              breakpoint: 1200,
              settings: {
                slidesToShow: 3
              }
            },
            {
              breakpoint: 1008,
              settings: {
                slidesToShow: 4
              }
            },
            {
                breakpoint: 800,
                settings: {
                  slidesToShow: 3
                }
              },
          ]
    })
});


// Prevent closing from click inside dropdown
$(document).on('click', '.dropdown-menu', function (e) {
  e.stopPropagation();
});

// clickable on mobile view
if ($(window).width() < 992) {
    $('.has-submenu a').click(function(e){
      e.preventDefault();
        $(this).next('.megasubmenu').toggle();

        $('.dropdown').on('hide.bs.dropdown', function () {
           $(this).find('.megasubmenu').hide();
        })
    });
}