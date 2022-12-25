buttons = document.querySelectorAll(".edit");
for (let i = 0; i < buttons.length; i++){
    buttons[i].addEventListener('click', displayEditBar)
}


function displayEditBar(){
    btnId = this.id;
    form = document.createElement("form");
    form.setAttribute("action", btnId)
    ok = document.createElement("button");
    ok.classList.add("ok");
    okTextNode = document.createTextNode("OK")
    ok.append(okTextNode);
    ok.setAttribute("type", "submit")
    ok.classList.add("btn", "btn-dark","mx-3");
    input = document.createElement("input");
    input.classList.add("form-control-lg");
    input.setAttribute("type", "text");
    input.setAttribute("name", "value");
    // input.addEventListener('input', function(){ inputText = input.value ; form.setAttribute("action", btnId+"/"+inputText)});
    form.append(input);
    form.append(ok)
    this.parentElement.parentElement.nextElementSibling.firstElementChild.append(form);
}

