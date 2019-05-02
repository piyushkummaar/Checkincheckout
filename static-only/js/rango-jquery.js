$("#btn").click(function(){
      var well = $("#id_location").val();
      if (well == ""){
       console.log("Entered if")
            alert("Enter a vaild address.");
      }
      else{
            $("#gmap_canvas").attr("src","https://maps.google.com/maps?q=" + well + "&t=&z=13&ie=UTF8&iwloc=&output=embed");
//            $("#gmap_canvas").attr("src","https://maps.google.com/maps?q=" + well + "canada&t=&z=13&ie=UTF8&iwloc=&output=embed");
    }
    });


// $( "#form1" ).on( "submit", function( event ) {
//            event.preventDefault();
//            console.log( $( this ).serialize() );
//        });

// $("#form1").on( "submit", function(e) {
//    e.preventDefault();
//    $.ajax({
//        type:'POST',
//        url:'/feedback/',
//        data:{
//            email:$('email').val(),
//            message:$('message').val(),
//        }
//        sucess:function(){
//        }
//    });
// });