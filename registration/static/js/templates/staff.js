var shirtSizes = [];
var departments = []; 
var divisions = []; 
let divDeps = {}; 


async function getOptionsFromJSON(path){
	let options = [];
	let rdata; 
	let multiOptions = false; 
	
	await $.getJSON(path, data =>{
		rdata = data; 
		$.each(data, function(key,val){
			let o = document.createElement('option');
				if(val.name == undefined){
					console.log('DATA IS',data);
					
					multiOptions = true; 
					oVal = Object.keys(data).indexOf(key);
					o.value = oVal;
					o.innerHTML = key;
					divDeps[key] = []; 
					for (v = 0; v < Object.keys(val).length; v++){ 
							k = Object.keys(val)[v];
							va = Object.values(val)[v]; 
							let to = document.createElement('option'); 
								to.innerHTML = va; 
								to.value = k; 
								divDeps[key].push(to); 
						
					}
				}
			
			else{
				o.value = val.id;
				o.innerHTML = val.name;
				 
			}
			options.push(o);
		});
		
	
	})
	if(multiOptions == true){
		let topMenu = []; 
		console.log(divDeps);
		let divs = await getOptionsFromJSON("/registration/divisions");
		let divData = divs.d; 
		
		for(k of Object.keys(divDeps)){
			let correctValue; 
			let topO = document.createElement('option');
			let index = Object.keys(divDeps).indexOf(k); 
			
			console.log(divData); 
			for(data of divData){
				if(data.name == k){
					correctValue = data.id;
					console.log("VAL IS ",correctValue); 
				}
			}
			
			
			topO.value = correctValue; 
			topO.innerHTML = k;
			topMenu.push(topO); 
		}
		
		
		
		return {'top': topMenu, 'secondary':divDeps}; 
	}
	return {'o':options,'d':rdata}; 
}



    $( "body" ).ready(async function() { 
		// only init the javascript datepicker if none is provided by the browser natively
        if (!Modernizr.inputtypes.date) {
            $("#birthDate").datepicker({
                format: 'yyyy-mm-dd',
                changeMonth: true,
                changeYear: true
            });
        }
	
		//Shirt size data.  
		let shirts = await getOptionsFromJSON("/registration/shirts");
		$("#shirt").append(shirts.o); 
		
		//Title data.  
		//Filter by group != 0 to avoid the chair team.   
		let titles = await getOptionsFromJSON("/registration/titles");
		titles.d.forEach(t=>{
			if(t.groupNo != 0){
				$('#title').append(titles.o[titles.d.indexOf(t)]);
		 }
		});
	
        //Division / Department data. 
		let divMap = await getOptionsFromJSON("/registration/divmaps");
		
		//console.log(divMap.top);
		
		$("#division").append(divMap.top); 
		
		var divs = await getOptionsFromJSON("/registration/divisions"); 
		$('#division').find('option').each((key, val)=>{
			let v = val.value;
			let divObj = divs.d[key];
			
			if(divObj != undefined){
				console.log(divObj.id); 
				let id = divObj.id; 
				val.value = id; 
				val.innerHTML = divObj.name
			}
			else{
				console.log("UNDEFINED",key,val); 
			}
		});


		  
		
		
		$('#division').on('change',e =>{
				//Clear out titles. 
				$('#title').find('option').remove(); 
						
				//Make the department container visible
				$(department).parent().parent().show(); 
				
				//Remove old options. 
				$('#department').find('option').remove();
					fO = document.createElement('option');
					fO.innerHTML = '-- Select One --' 
					fO.value=''; 
					department.appendChild(fO); 
				
				
				let index = e.currentTarget.selectedIndex; 
				let value = $('#division').children().eq(index)[0].textContent;
				let options = divMap.secondary[value];

				if(value != "-- Select One --"){
					//If chair team, remove department; change titles.  
					if(value == "Chair Team"){
						//Replace the titles w/ char team titles. 
						titles.d.forEach(t=>{
							if(t.groupNo != 1){
								$('#title').append(titles.o[titles.d.indexOf(t)]);
							}
						});
						
						
						//Prevents the warning from appearing.  
						$(department).parent().parent().hide();  
						$("#department").find('option').eq(0)[0].value = 'CHAIR TEAM'
						$("#department").focus().click().blur(); 
						$(title).focus().click().blur(); 
					}
					
					
					else{
						//Set titles.
						titles.d.forEach(t=>{
							if(t.groupNo != 0){
								$('#title').append(titles.o[titles.d.indexOf(t)]);
							}
						});
						
						for(let o = 0; o < Object.keys(options).length;o++){
							let key = Object.keys(options)[o]; 
							
							
							let value = Object.values(options)[o]; 
							department.appendChild(value);	
						}
					
					
					}
				}
				
				
				
				else{
					titles.d.forEach(t=>{
							if(t.groupNo != 0){
								$('#title').append(titles.o[titles.d.indexOf(t)]);
							}
						});
				
				}
				$('#department').replaceWith(department);
			}); 
			
			$('#title').on('change',e =>{
				$(department).parent().parent().show(); 
				let index = e.currentTarget.selectedIndex; 
				let value = $('#title').children().eq(index)[0].textContent;
				let options = divMap.secondary[value];
				
				if(value == "Vice Convention Chair" || value == "Convention Chair"){
					$(department).parent().parent().hide(); 
				}
				
				if(value == "Division Head"){
					$(department).parent().parent().hide(); 
					$("#department").find('option').eq(0)[0].value = 'DIV HEAD'
					$(department).focus().click().blur(); 
					
				} 
			});
	});
	$('.aDesc').hide();
	$('#whitelist').parent().parent().hide();
	$('#blacklist').parent().parent().hide();
	
	$("#accommodation").on("change",function(e){
		$('.aDesc').hide();
		let index = e.currentTarget.selectedIndex; 
		let value = $('#accommodation').children().eq(index)[0].value;
		console.log(value); 
		$(`.aDesc.${value}`).show(); 
		
		
		if(value == 0){
			$('#whitelist').parent().parent().show();
			$('#blacklist').parent().parent().show();
		}
		else{
			$('#whitelist').parent().parent().hide();
			$('#blacklist').parent().parent().hide();
		}
		
	});

    $("#country").on("change", function() {
        if ($(this).val() == "US"){
            $("#state").removeAttr("disabled").attr("required", "required");
            $("#state").find('option').eq(0).html("-- Select One --")
            $("#zip").val("").removeAttr("disabled").attr("required", "required");
        } else {
            $("#state").val("").attr("disabled", "disabled").removeAttr("required");
            $("#zip").val("").attr("disabled", "disabled").removeAttr("required");
        }
    });
