function show_filter() {
    let form = document.getElementById('form_filter')
    form.style.display = 'block';
}
document.addEventListener('DOMContentLoaded', function() {
    var e = document.getElementById('department1');
    var value = e.value;
    var text = e.options[e.selectedIndex].text;
    console.log(text)
    if (text === "All") {
        document.getElementById('form_filter').style.display = 'none';
        console.log('tester')
    } else {
        show_filter()
        console.log('teste1r')

    }
})

function ChecklistView(result, id) {
    console.log(result)
    console.log(id)

    // Title
    document.querySelector(`#title_${id}`).innerHTML = result.checklist[0]
    document.querySelector(`#title_${id}`).innerHTML = result.checklist[0]

    // Description
    document.querySelector(`#description_${id}`).innerHTML = result.checklist[1];

    // Badge
    document.querySelector(`#badge_${id}`).innerHTML = result.checklist[2]

    // Checkboxes
    check = document.querySelector(`#checks_${id}`)
    check_clear = document.querySelector(`#checks_${id}`).children
    check.replaceChildren();
    for (let i = 0; i < result.items.length; i++) {
        const element = document.createElement('input');
        element.type = "checkbox"
        element.name = i
        check.append(element);
        const element2 = document.createElement('label');
        element2.for = i
        element2.innerHTML = "  " + result.items[i]
        element2.style.marginLeft = "10px";
        check.append(element2);
        const element3 = document.createElement('br');
        check.append(element3);
    }
}

function fetcher(id) {
    console.log(id)
    fetch(`/home/checklistView/${id}`)
    .then(response => response.json())
    .then(result => ChecklistView(result, id))
}

