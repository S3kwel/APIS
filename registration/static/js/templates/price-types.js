var levelTemplateData = [];
var levelData = [];
var shirtSizes = [];
var adult; 
var converter = new showdown.Converter()
//NOTE: Templates for attendee reg are located ???


$( "body" ).ready(function() { 
		optionImage = []; 
		
		var url = "/registration/pricelevels";
        if(adult != undefined){
            url = "/registration/adultpricelevels";
        }
		
		
		
        $.getJSON(url, function(data) {
			var option_img = {};
            levelData = data;
			console.log(data); 
            $.each( data, function( key, val ) {
                var price = val.base_price;
				option_img['id'] = val.id;
				option_img['val'] = val.optionImage;
				optionImage.push(option_img); 
                if (typeof discount != 'undefined') { price = val.base_price - discount; }
               
				levelTemplateData.push({
                    name: val.name,
                    price: "$" + price,
                    levelId: "level_" + val.id,
                    selectText: "Select " + val.name,
					img: val.optionImage, 
                });
            });
            $("#levelContainer").loadTemplate($("#levelTemplate"), levelTemplateData, {afterInsert: d=>{setBg(d)}});
            $(".changeLevel").hide();
        });

        $.getJSON("/registration/shirts", function(data) {
            shirtSizes = data;
			if(shirtSizes.length == 0){
				console.warn("EM: No shirt sizes found!");
			}
        });
		
	

});
	
	//TODO: Is there a better way to do this than to just hand the var to each scope? 
    $("#levelContainer").off().on('click', 'a.selectLevel', function(){
		clearLevels();
		var levelId = $(this).attr('id').split('_')[1];
		var oI = optionImage; 
		
		$.each( levelTemplateData, function( key, val ) {
            var id = val.levelId.split('_')[1];
			console.log(id); 
			console.log(levelId); 
            
			if (id == levelId){
                $("#regLevel").val(val.name);
                $("#levelContainer").loadTemplate($("#levelTemplate"), val,{afterInsert: d=>{setBg(d)}});
                $(".changeLevel").show();
                $(".selectLevel").hide();
                generateOptions(id);
				alert(oI[id].val); 
				setBg($("#levelTemplate"),oI[id].val); 
				
				
                return false;
            }
			else{}
			
        });
    });
	
    $("#levelContainer").on('click', 'a.changeLevel', function() {
        $("#levelContainer").loadTemplate($("#levelTemplate"), levelTemplateData, {afterInsert: d=>{setBg(d)}});      
        $("#regLevel").val("");
        $(".changeLevel").hide();
    });
	
    var clearLevels = function(){
        $.each( levelTemplateData, function( key, val ) {
            $("#"+val.levelId).text("Select " + val.name);
        });
        $("form").validator('update');
    };
	
	var setBg = function(d,img){
			if(typeof img == 'undefined'){
				img = $(d).find('.priceImg').attr('src');
			} 
			else{
				alert('else');
				console.log(img); 
			}
			//img = $(d).find('.priceImg').attr('src');
			$(d).find('.priceImg').remove();
			console.log(img); 
			console.log(d); 
			$(d).find('.panel.price').css('background-image',`linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ),url(${img})`); 
		}
	
    var generateOptions = function(levelId){
        var data = [];
        var description = "";
        $.each(levelData, function(key, thing){
            if (thing.id == levelId){
                data = thing.options;
                description = converter.makeHtml(thing.description);
                return false;
            }
        });
		
		//NOTE: Why not template this out at some point?
		var container = $("<div id='optionsContainer' class='col-xs-6 col-sm-6 col-md-6 col-lg-8'><h4>Description</h4><hr/><div class='form-group'><div class='col-sm-12'>" + converter.makeHtml(description) + "<div class ='row addons' ><h5 class='text-center'><b>Add-ons</b></h5><hr></div></div></div></div>");
		$("#levelContainer").append(container);
		if(data.length == 0){$(".row.addons").remove();
		} 
        $.each( data, function(key, val) {
			
            if (val.value == "0.00"){var price = " (Free) ";}
			else {
                var price = " (+$" + val.value + ") "
            }
            var required = "";
            if (val.required) {required = "required";}
            
			var template = $("#optionBoolTemplate");
			if (val.required) {template = $("#optionBoolReqTemplate");}
			console.log(val); 
			$("#optionsContainer").loadTemplate(template, {
				'name': val.name + " " + price,
				'id': "option_" + val.id,
				'description': val.description
			}, {append: true});
		
        });
		$('.addons').append(
		`<div class = 'col-xs-4'><i>Name</i></div>
		<div class = 'col-xs-8'><i>Description</i></div>
		
		`)

        $("form").validator('update');
    };

   var getOptions = function() {
        var options = $(".levelOptions");
                var data = [];
        $.each(options, function(key, option) {
            if ($(option).is(':checkbox')) {
                if ($(option).is(':checked')) {
                    data.push({'id': option.id.split('_')[1], 'value': $(option).is(':checked')});
                }
            } else {
                if ($(option).val() != "") {
                    data.push({'id': option.id.split('_')[1], 'value': $(option).val()});
                }            
            }
        });
        return data;
    };

