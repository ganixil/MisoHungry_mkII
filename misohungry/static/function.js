function addMaterial(){
	var input = document.createElement('input');
	input.type = 'text';
	input.name = 'material';
	input.className = 'form-control';
	
	var br = document.createElement('br');
	var inputField = document.getElementById('input_wrapper');
	inputField.appendChild(input);
	inputField.appendChild(br);
}