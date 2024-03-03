// -----------------------------

//   JS INDEX
/* =================== */
/* 

    ## Preloader
    ## sticky
    ## S 
    ## Dropdown 
    ## Counter Up
    ## Video
    ## Googel Map
    ## Shuffle Js

*/

/* (function($) {
  "use strict"; */

  
/**=========== Hamburger Menu ========**/

$(window).on('load', function(){
	$('.navbar-toggler').click(function(){
    $('.navbar-toggler').toggleClass('nav-icon');
	});
});

//**========== End-Hamburger Menu ===========**//

//**================== Preloder========================*//

  $(window).on('load', function() {
    $('.preloader').fadeOut('slow', function() { $(this).remove(); });
  });

//**================= End of Preloder =====================**//

//**================= Sticky =====================**//

$(window).on('scroll', function() {
  if ($(window).scrollTop() > 50) {
      $('.header-area').addClass('nav-fixed');
  } else {
      $('.header-area').removeClass('nav-fixed');
  }
});

//**=================End Sticky =====================**//

//*==================nav Click Animation================= *//

   /*---------------------
    smooth scroll
    --------------------- */

    if (jQuery('.smoothscroll').length > 0) {   
    $('.smoothscroll').on('click', function(e) {
      e.preventDefault();
      var target = this.hash;

      $('html, body').stop().animate({
          'scrollTop': $(target).offset().top - 80
      }, 1200);
  });
}

//*===============End nav Click Animation==================*//

//**=================Dropdown=====================**//




$(window).on('load', function() {

  if($(".navbar-nav li.nav-item ul li").has("ul").length) {
      $('.navbar-nav li.nav-item ul li ul').parent().addClass('dd-caret');
  }

  $('li.dd-caret').on('click', function(){
    
    $('li.dd-caret').removeClass('dd-active');
    $(this).addClass('dd-active');
    $('.dd-active').parent('ul.dropdown-menu').addClass('show');
    
    $('li.dd-caret').children('ul').removeClass('shownav');
    $(this).children('ul').addClass('shownav');
    
  })

});


$('.navbar-nav>li.nav-item>a').on('click', function(){
  // $('.navbar-nav li .dropdown-menu').removeClass('shownav');
  
  $('.navbar-nav>li.nav-item>a').siblings('ul.dropdown-menu').removeClass('shownav');
 

})




$('.navbar-nav li.nav-item ul li.dropdown-item').on('click', function(){
  // $('.navbar-nav>li.nav-item ul').removeClass('shownav');
  $(this).parent('ul').addClass('shownav');
  $(this).parent('ul').parent().addClass('shownav');

 

})






// nav-item
 
//**=================End Dropdown=====================**//

//**================= CounterUp =====================**//
if (jQuery('.counterUp').length > 0) {   
  jQuery('.counterUp').counterUp({
      delay: 10,
      time: 1000
  });
}

//**================= End CounterUp =====================**//

//*Animation js *//

//**=================== WOW ================================**//
   var wowSel = 'wow';
   var wow = new WOW({
       boxClass: wowSel,
       animateClass: 'animated',
       offset: 0,
       mobile: true,
       live: true,
       callback: function(box) {
       },
       scrollContainer: null
   });
   wow.init();

//**============== End of WOW =============================**//


//**==================Video Play- Pause-Stop===================================**//
if (jQuery('.video').length > 0) {   
var player;
function onYouTubePlayerAPIReady() {
  player = new YT.Player('video', {
    events: {
      'onReady': onPlayerReady
    }
  });
}
function onPlayerReady(event) {
  var pauseButton = document.getElementById("pause-button");
  var fullbody = document.querySelector('body');
  
  pauseButton.addEventListener("click", function() {
    player.pauseVideo();
    
  });

  fullbody.addEventListener("click", function() {
    player.pauseVideo();
    
  });
}
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
}

//***================== End YouTube Video Pause-Play-Stop =============******//

//**=================== Google Map ==========================**//

if (jQuery('#googleMap').length > 0) {   
var user_lat, user_lng;
    var map;
    var grayStyles = [
      {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
      {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
      {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
      {
        featureType: 'administrative.locality',
        elementType: 'labels.text.fill',
        stylers: [{color: '#d59563'}]
      },
      {
        featureType: 'poi',
        elementType: 'labels.text.fill',
        stylers: [{color: '#d59563'}]
      },
      {
        featureType: 'poi.park',
        elementType: 'geometry',
        stylers: [{color: '#263c3f'}]
      },
      {
        featureType: 'poi.park',
        elementType: 'labels.text.fill',
        stylers: [{color: '#6b9a76'}]
      },
      {
        featureType: 'road',
        elementType: 'geometry',
        stylers: [{color: '#38414e'}]
      },
      {
        featureType: 'road',
        elementType: 'geometry.stroke',
        stylers: [{color: '#212a37'}]
      },
      {
        featureType: 'road',
        elementType: 'labels.text.fill',
        stylers: [{color: '#9ca5b3'}]
      },
      {
        featureType: 'road.highway',
        elementType: 'geometry',
        stylers: [{color: '#746855'}]
      },
      {
        featureType: 'road.highway',
        elementType: 'geometry.stroke',
        stylers: [{color: '#1f2835'}]
      },
      {
        featureType: 'road.highway',
        elementType: 'labels.text.fill',
        stylers: [{color: '#f3d19c'}]
      },
      {
        featureType: 'transit',
        elementType: 'geometry',
        stylers: [{color: '#2f3948'}]
      },
      {
        featureType: 'transit.station',
        elementType: 'labels.text.fill',
        stylers: [{color: '#d59563'}]
      },
      {
        featureType: 'water',
        elementType: 'geometry',
        stylers: [{color: '#17263c'}]
      },
      {
        featureType: 'water',
        elementType: 'labels.text.fill',
        stylers: [{color: '#515c6d'}]
      },
      {
        featureType: 'water',
        elementType: 'labels.text.stroke',
        stylers: [{color: '#17263c'}]
      }
    ]

    function initMap() {
        map = new google.maps.Map(document.getElementById('googleMap'), {
            center: {
                lat: 23.782062,
                lng: 90.416053
            },
            zoom: 15,
            scrollwheel: false,
            styles: grayStyles
        });
              
      var marker = new google.maps.Marker({
        position:  {  lat: 23.782062, lng: 90.416053},
        map: map,
        icon: "assets/images/gmap.png"
      });

          } 

        }
//*================ End Google Map ============*//

//*================ Portfolio Shuffle ============*//

var Shuffle = window.Shuffle;

if($('.my-shuffle-container').length > 0){
  var element = document.querySelector('.my-shuffle-container');
  var sizer = element.querySelector('.my-sizer-element');

  var shuffleInstance = new Shuffle(element, {
    itemSelector: '.single-portfolio',
  });
  $("#all").on("click", function(){
    shuffleInstance.filter();
  });
  $("#design").on("click", function(){
    shuffleInstance.filter('design');
  });
  $("#photography").on("click", function(){
    shuffleInstance.filter('photography');
  });
  $("#ui-design").on("click", function(){
    shuffleInstance.filter('ui-design');
  }); 
  $("#ux-design").on("click", function(){
    shuffleInstance.filter('ux-design');
  });
  $("#branding").on("click", function(){
    shuffleInstance.filter('branding');
  });
}

//*================End Portfolio Shuffle ============*//

//*================Portfolio-2 Shuffle ============*//

if($('.my-shuffle-container2').length > 0){

  // var Shuffle2 = window.Shuffle;
  var element2 = document.querySelector('.my-shuffle-container2');
  var sizer2 = element2.querySelector('.my-sizer-element2');
  var shuffleInstance2 = new Shuffle(element2, {
    itemSelector: '.single-portfolio2',
    sizer: sizer2
  });
  $("#all-2").on("click", function(){
    shuffleInstance2.filter();
  });
  $("#design-2").on("click", function(){
    shuffleInstance2.filter('design-2');
  });
  $("#photography-2").on("click", function(){
    shuffleInstance2.filter('photography-2');
  });
  $("#ui-design-2").on("click", function(){
    shuffleInstance2.filter('ui-design-2');
  }); 
  $("#ux-design-2").on("click", function(){
    shuffleInstance2.filter('ux-design-2');
  });
  $("#branding-2").on("click", function(){
    shuffleInstance2.filter('branding-2');
  });
}

//**================ End Portfolio-2 Shuffle ============**//




/*---------------------
    // Ajax Contact Form
    --------------------- */


    $('.cf-msg').hide();
    $('form#cf button#submit').on('click', function() {
    
        var firstName = $('#firstName').val();
        var phone = $('#phone').val();
        var email = $('#email').val();
        var subjectName = $('#subjectName').val();
        var msg = $('#msg').val();
        var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    
        if (!regex.test(email)) {
            alert('Please enter valid email');
            return false;
        }
    
        firstName = $.trim(firstName);
        phone = $.trim(phone);
        subjectName = $.trim(subjectName);
        email = $.trim(email);
        msg = $.trim(msg);
    
        if (firstName != '' && email != '' && msg != '') {
            var values = "firstName=" + firstName + "&phone=" + phone + "&subjectName=" + subjectName + "&email=" + email + " &msg=" + msg;
            $.ajax({
                type: "POST",
                url: "assets/php/mail.php",
                data: values,
                success: function() {
                    $('#firstName').val('');
                    $('#phone').val('');
                    $('#subjectName').val('');
                    $('#email').val('');
                    $('#msg').val('');
    
                    $('.cf-msg').fadeIn().html('<div class="alert alert-success"><strong>Success!</strong> Email has been sent successfully.</div>');
                    setTimeout(function() {
                        $('.cf-msg').fadeOut('slow');
                    }, 4000);
                }
            });
        } else {
            $('.cf-msg').fadeIn().html('<div class="alert alert-danger"><strong>Warning!</strong> Please fillup the informations correctly.</div>')
        }
        return false;
    });
    
    
    // Ajax Contact Form JS END


    // Estimate Calculator JS
      $('#estimate-btn').on('click', function(){

        if ($('#wd-height').val().length > 0 && $('#wd-height').val().length > 0) {
            var wallwidth = parseInt($('#wd-height').val());
            var wallheight = parseInt($('#wd-width').val());
            var totalwalldimension = wallwidth * wallheight;

            var windowwidth = parseInt($('#wnd-width').val());
            var windowheight = parseInt($('#wnd-height').val());
            var totalwindowdimension = windowwidth * windowheight;

            var doorwidth = parseInt($('#doord-width').val());
            var doorheight = parseInt($('#doord-height').val());
            var totaldoordimension = doorwidth * doorheight;
            
            
            var totaldoorandwindow = totaldoordimension + totalwindowdimension;

            var walldimensionresult = totalwalldimension - totaldoorandwindow;


            // doubledoor-qty coat-qty-check
            var doorwidth = parseInt($('#mitresquireperlitre').text());

            var paintcoat = $("input[name='coat-qty-check']:checked").val();

            var totalLitreneed = walldimensionresult / doorwidth;

                totalLitreneed = totalLitreneed * paintcoat;
                totalLitreneed = totalLitreneed.toFixed(2) ;

            $('#litre-result').text(totalLitreneed);

            
        }

    })


    $('#estimate-reset-btn').on('click', function(){
        $('#wd-height').val('0.00');
        $('#wd-width').val('0.00');
        $('#wnd-width').val('0.00');
        $('#wnd-height').val('0.00');
        $('#doord-width').val('0.00');
        $('#doord-height').val('0.00');
        $('#litre-result').text('00.00');
    })
    // Estimate Calculator JS END

/* }(jQuery)); */






