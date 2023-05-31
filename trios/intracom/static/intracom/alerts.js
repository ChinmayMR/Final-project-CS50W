function AlertView(result, id) {
    console.log()
    // Title
    document.querySelector(`#title_${id}`).innerHTML = result.alert[0]

    // Description
    description = result.description
    console.log(description)
    for (var line in description) {
        if (description[line] === '') {
            // console.log("empty line detected")
            // console.log(description[line])
            // console.log("empty line detected")  
            description[line] = "<br>";
        }
        else {
            x = description[line] + "<br>"
            console.log(x)
            description[line] = x
        }
    }
    // console.log(description.join(''))
    document.querySelector(`#description_${id}`).innerHTML = description.join('')

    // Badge
    document.querySelector(`#badge_${id}`).innerHTML = result.alert[3]

    // // Checkboxes
    // check = document.querySelector(`#checks_${id}`)
    // for (let i = 0; i < result.items.length; i++) {
    //     const element = document.createElement('input');
    //     element.type = "checkbox"
    //     element.name = i
    //     check.append(element);
    //     const element2 = document.createElement('label');
    //     element2.for = i
    //     element2.innerHTML = "  " + result.items[i]
    //     element2.style.marginLeft = "10px";
    //     check.append(element2);
    //     const element3 = document.createElement('br');
    //     check.append(element3);
    // }
}

function fetcher(id) {
    console.log(id)
    fetch(`/home/alertView/${id}`)
    .then(response => response.json())
    .then(result => AlertView(result, id))
}