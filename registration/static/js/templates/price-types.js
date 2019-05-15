var levelTemplateData = [];
var levelData = [];
var shirtSizes = [];
var adult; 
var converter = new showdown.Converter()
//NOTE: Templates for attendee reg are located ???


$( "body" ).ready(function() { 
		var url = "/registration/pricelevels";
        if(adult != undefined){
            url = "/registration/adultpricelevels";
        }
		
		
		
        $.getJSON(url, function(data) {
            levelData = data;
			console.log(data); 
            $.each( data, function( key, val ) {
                var price = val.base_price;
			
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

    $("#levelContainer").on('click', 'a.selectLevel', function(){
        clearLevels();
        var levelId = $(this).attr('id').split('_')[1];
        $.each( levelTemplateData, function( key, val ) {
            var id = val.levelId.split('_')[1];
            if (id == levelId){
                $("#regLevel").val(val.name);
                $("#levelContainer").loadTemplate($("#levelTemplate"), val,{afterInsert: d=>{setBg(d)}});
                $(".changeLevel").show();
                $(".selectLevel").hide();
                generateOptions(id);
                return false;
            }
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
	
	var setBg = function(d){
			let img = $(d).find('.priceImg').attr('src');
			$(d).find('.priceImg').remove();
			let w = $(d).find('.panel.price').outerWidth();
			let h = $(d).find('.panel.price').outerHeight() * 0.86;
			$(d).find('.panel.price').css('background-position',`center top`); 
			$(d).find('.panel.price').css('background-size',`100%`); 
			$(d).find('.panel.price').css('background-opacity',`0.5`); 
			$(d).find('.panel.price').css('background-repeat',`no-repeat`); 
			$(d).find('.panel.price').css('background-image',`url(${img})`); 
			$($(d).find('.panel.price')).prepend(`<div class ='priceOptionCover' style='position: absolute; z-index: 0; pointer-events:none; background-color: black; opacity: 0.5; width: ${w}px; height: ${h}px; '></div>`);
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
		//TODO: Gut this system. The model is weird and the implementation is awkward. 
        var container = $("<div id='optionsContainer' class='col-xs-6 col-sm-6 col-md-6 col-lg-8'><h4>Description</h4><hr/><div class='form-group'><div class='col-sm-12'>" + converter.makeHtml(description) + "</div></div></div>");
        $("#levelContainer").append(container);
        $.each( data, function(key, val) {
            if (val.value == "0.00"){var price = " (Free) ";}
			else {
                var price = " (+$" + val.value + ") "
            }
            var required = "";
            if (val.required) {required = "required";}
            
			var template = $("#optionBoolTemplate");
			if (val.required) {template = $("#optionBoolReqTemplate");}
			$("#optionsContainer").loadTemplate(template, {
				'name': val.name + " " + price,
				'id': "option_" + val.id
			}, {append: true});
        });

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

