// $.validator.setDefaults( {
//     submitHandler: function () {
//        alert( "submitted!" );
//     }
//  });


$(function () {
   $("#form1").validate({
      rules: {

         nombre: {
            required: true,
            minlength: 5
         },

         apellido: {
            required: true,
            minlength: 5
         },

         rut: {
            required: true
         },


         email: {
            required: true,
            email: true
         },


         contrasena: {
            required: true,
            minlength: 5
         },




         //   confirm_password: {
         //      required: true,
         //      minlength: 5,
         //      equalTo: "#password"
         //   },



         invalidCheck: "required"
      },







      messages: {

         nombre: {
            required: "Por favor ingresa tu nombre",
            minlength: "Tu nombre debe ser de no menos de 5 caracteres"
         },


         apellido: {
            required: "Por favor ingresa tu apellido",
            minlength: "Tu nombre debe ser de no menos de 5 caracteres"
         },

         rut: {
            required: "Por favor ingresa tu Rut",

         },





         //   comments: "Por favor ingresa un comentario",
         //   password: {
         //      required: "Por favor ingresa una contraseña",
         //      minlength: "Tu contraseña debe ser de no menos de 5 caracteres de longitud"
         //   },
         //   confirm_password: {
         //      required: "Ingresa un password",
         //      minlength: "Tu contraseña debe ser de no menos de 5 caracteres de longitud",
         //      equalTo: "Por favor ingresa la misma contraseña de arriba"
         //   },

         email: "Por favor ingresa un correo válido",

         contrasena: {
            required: "Por favor ingresa tu Contraseña",
            minlength: "Tu Contraseña debe ser de no menos de 5 caracteres"
         },

         invalidCheck: "Por favor Acepta términos y condiciones",



         luckynumber: {
            required: "Por favor"
         }
      },




      //  errorElement: "em",
      //  errorPlacement: function (error, element) {
      //     // Add the `help-block` class to the error element
      //     error.addClass("help-block");

      //     if (element.prop( "type" ) === "checkbox") {
      //        error.insertAfter(element.parent("label") );
      //     } else {
      //        error.insertAfter(element);
      //     }
      //  },
      //  highlight: function ( element, errorClass, validClass ) {
      //     $( element ).parents( ".col-sm-10" ).addClass( "has-error" ).removeClass( "has-success" );
      //  },
      //  unhighlight: function (element, errorClass, validClass) {
      //     $( element ).parents( ".col-sm-10" ).addClass( "has-success" ).removeClass( "has-error" );  
    
    });
 });
