console.log('element');

var Element = function(options){
	Element.instances++; //Should serve as a unique ID for each element.  
	this.instances = Element.instances; 
	//Messages
	this.messages = {
		noName: `Your field has no name set!`,
		noType: `Type not set for an element that needs it.`,
		noOptions: `No options have been provided!`
	}
	
	this.html = document.createDocumentFragment(); 
	let input; 
	let label; 
	if(typeof options != 'object' || typeof options == 'undefined'){throw(this.messages.noOptions);}
	
	
	//Internal options.
	this.addWrapper = options.addWrapper !== undefined ? options.addWrapper : true; 
	this.options = options.options != undefined ? options.options : [];
	this.addToggle = options.addToggle != undefined ? options.addToggle : false; 
	
	//Element-related options.  
	this.element = options.element !== undefined ? options.element : null;
	this.name = options.name !== undefined ? options.name : null;
	this.displayName = options.displayName !== undefined ? options.displayName : null;
	this.label = options.label !== undefined ? options.label : null;
	this.branchLevel = options.branchLevel != undefined ? options.branchLevel : 0; 
	this.text = options.text != undefined ? options.text : null; 
	this.properties = options.properties != undefined ? options.properties : null;  
	this.selectOptions = options.selectOptions != undefined ? options.selectOptions : false; 
	this.radioOptions = options.radioOptions != undefined ? options.radioOptions : false; 
	
	this.name = options.name !== undefined ? options.name : null;
	
	//Create a wrapper div to be sent with the return data, if this.addWrapper is true.  
	//This should represent the top-level target for each element for CSS purposes; even if it contains multiple child elements.  
	if(this.addWrapper){
		this.wD = document.createElement('div');
	
		
		//Clean up the title if it isn't suitable for a className
		if(this.name != null && this.name.split(' ').length > 1){
			let words = this.name.split(' ');
			this.name = '';
			for (w of words){this.name += `${w}-`;}
			this.name = this.name.substring(0,this.name.lastIndexOf('-'));
		}
		
		this.wD.className = `modal__content__wrapper ${Element.instances} ${this.name}`;
	}
	else{
		this.wD = document.createDocumentFragment(); 
	}
	
	
	/* Create a single element.
		1. Create the base element, name it.  
		2. Append text if it has been provided.
		3. Get any properties (e.g. type, src,etc.) that have been provided.
		4. Determine whether a type has been provided for elements that need it.
		5. Check if the element is a select. Check for options if so.  
		6. Flush properties into the base element.
		7. If addToggle is on, add a check box before the element.  
		8. If a label has been provided, add it. Otherwise, just add the element.
	*/
	
	let self = this; 
	this.single = function(changeHandler = null){
		
		
		Element.singleInstances++ //Unique ID for specific single element.  
		this.singleInstances = Element.singleInstances;
		var sElement = document.createElement(this.element);
		sElement.className = `v ${this.name} ${this.instances}`; 
		
		
		sElement.innerHTML = this.text; 
		
		let keys = this.properties != undefined ? Object.keys(this.properties) : 0;
		let vals = this.properties != undefined ? Object.values(this.properties): 0; 
		
		
		if(this.element == "input"){
			if(this.properties == null || options.properties['type'] == undefined){
				throw(this.messages.noType);
			}
		}
		
		if(this.element == "select" && (this.selectOptions != undefined || this.selectOptions.length != 0)){
			for(let i in this.selectOptions){
				let o = this.selectOptions[i];
				let op = document.createElement('option');
				op.value = o;
				op.innerHTML = o; 
				sElement.add(op);
			}
		}
		for(i in keys){sElement[keys[i]] = vals[i];}
		
		if(this.addToggle){
			let toggle = document.createElement("input");
			toggle.type = "checkbox"; 
			
			toggle.className = `t ${this.name} ${this.singleInstances}`; 
			this.wD.append(toggle); 
		}
	
		if(changeHandler != null){
			$(sElement).on("change",changeHandler);
		}
		
		if(this.label != undefined){
			let label = document.createElement("label");
			label.htmlFor = this.name; 
			label.innerHTML = " " + this.label + " "; 
			this.wD.append(label,sElement);
		}
		else{
			this.wD.append(sElement);
		}
		
		return this.wD;
	}
	
	
	
	//Uses the JSON at path to create a set of selects which appear/disappear depending on the choices the user makes.  
	this.branch = async function(path){
		let json = path; 
		let container = document.createElement('div');
		container.className = 'container-fluid';
		
		for(let i = 0; i < this.branchLevel; i++){
			//Containing Div
			let div = document.createElement('div');
			div.className = `swr ${this.name} ${i} row`;
			
			let headerRow = document.createElement('div');
			headerRow.className = `hr ${this.name} ${i} row`;
			
			
			let headerCol = document.createElement('div');
			headerCol.className = `hr ${this.name} ${i} col`;
			
			let header = document.createElement('h6');
			header.className = '';
			header.innerText = this.displayName
			headerCol.append(header);
			
			headerRow.append(headerCol);
			
			
			//div.append(headerRow);
			
			//Select container (to hold labels/toggles/etc)
		
			
			//Col
			let col = document.createElement('div');
			col.className = 'col-5';
			
			
			//Select
			let s = document.createElement('select');
			s.className = `v ${this.name} form-control ${i}`;
			s.name = `action-${this.label[i].replace(/:/g,"").toLowerCase()}`;
			
			
			
			
			if(this.addToggle == true || this.label != null){
				if(this.addToggle == true){
					let t = document.createElement('input');
					t.dataset.associate = `action-${this.label[i].replace(/:/g,"").toLowerCase()}`;
					let l = document.createElement('label');
					l.className='checkbox-inline';
					
					t.className = `t ${this.name} ${i}`;
					t.name = `toggle-${this.label[i].replace(/:/g,"").toLowerCase()}`;
					t.type = 'checkbox';
					l.append(t);
					col.append(l);
					
				}
				
				if(this.label != null){
					let l = document.createElement("label");
					l.htmlFor = `${this.name} ${i}`
					l.innerHTML =`${this.label[i]} `;
					l.className = 'form-check-label text-dark';
					col.append(' ',l);
				}
				
				let colTwo = document.createElement('div');
				colTwo.className ='col-7';
				div.append(s);
				
				colTwo.append(s); 
				
				
				div.append(col);
				div.append(colTwo);
				//div.append(sDiv);
			}
			else{
				div.append(s);
			}
			
			//Toggle
			
			//Label
			
			if(i == 0){
				container.append(headerRow);
			}
			container.append(div);
			this.wD.append(container);
		}
		console.log(this.name); 
		const selects = [...$(`select.${this.name}`,this.wD)];

		this.populateDropDown = function(obj, i) {
			if(Object.keys(obj).length != 0){
				for(let i = 0; i < selects.length; i++){$(selects[i]).parent().css('display','block');}
			}
			else{
			
			}
			
			
			selects[i].innerHTML = obj && Object.keys(obj).length ? null : $(selects[i]).parent().css('display','none'); $(selects[i]).parent().children('input').prop('checked', false);
			
			if(selects[i].innerHTML == null){
				$(selects[i]).css('display','none');
			}
			
			for (const key in obj) {
				const option = document.createElement("option");
				option.text = key;
				selects[i].add(option); 
			}
		}
		
		let self = this;
		this.makeSelection = function(e) {
			let sub = json;
			const j = selects.indexOf(e.target)+1;
			
			selects.forEach((sel, i) => {
				if (i === j) self.populateDropDown(sub, i); 
				if (i > j) sel.innerHTML = "";
				sub = sub && sel.selectedIndex >= 0 && sub[sel.options[sel.selectedIndex].textContent];
				
			});
			$(selects[j]).change();
		
			
		}
		for (const sel of selects){
			$(sel).on('change', this.makeSelection);
		} 
		
		
		this.populateDropDown(json, 0);
		$(selects[0]).change();
		return this.wD;
		
	}
	
	//Loads icons from path as buttons. 
	/*
	* Chrome offers no file system access to extensions.  
	* This system works by assuming there will be numbered icons up to this.max at path. 
	*/
	this.icons = async function(path){
		this.guid = function() {
		  function s4() {
			return Math.floor((1 + Math.random()) * 0x10000)
			  .toString(16)
			  .substring(1);
		  }
		  return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4();
		}
		this.returnData = {}; 
		
		this.max = 70;
		this.imageFolder = chrome.extension.getURL(`/images${path}/`);
		
		
		for(let i = 1; i < this.max; i++){
			let fileName = `${this.imageFolder}${i}.png`;
			try{let file = await $.get({url: fileName});}
			catch{
				this.max = i;
				for(let i = 1; i < this.max; i++){
					let gid = this.guid(); 
					let fileName = `${this.imageFolder}${i}.png`;
					//let id = i; 
					let style = `background-image: url(${fileName});`
					let html = `<div class='quick-action ${gid}' title="button ${i}" style="${style}"></div>`; 
					this.returnData[i] = {id: `.quick-action.${gid}`, style: style, html: `${html}`, enabled: "true"};
				}
			}
		}
		
		
		for(let i = 0; i < Object.values(this.returnData).length; i++){
			let dd = Object.values(this.returnData)[i];
			$(this.wD).append(dd.html);
			
			$(`body`).on('click',`${dd.id}`,function(){
				$(`.modal__content__wrapper .quick-action, .modal__content__wrapper .quick-action:hover`).addClass('deselected');
				$(`${dd.id}`).removeClass('deselected'); 
			});
		}
		
		//console.log(this.returnData);
		return this.wD;
		
	}
		
}
Element.instances = 0; 
Element.singleInstances = 0; 