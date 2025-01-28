function searchItems() {
    let input, filter, items, item, h2, i, txtValue, containers, noResultsMessage;
    input = document.getElementById('searchInput');
    filter = input.value.toLowerCase();
    containers = document.getElementsByClassName('coffee-items');
    noResultsMessage = document.getElementById('noResultsMessage');
    
    let hasVisibleItemsOverall = false;

    for (let j = 0; j < containers.length; j++) {
        let container = containers[j];
        items = container.getElementsByClassName('coffee-item');
        let hasVisibleItems = false;
        
        for (i = 0; i < items.length; i++) {
            item = items[i];
            h2 = item.getElementsByTagName('h2')[0];
            if (h2) {
                txtValue = h2.textContent || h2.innerText;
                if (txtValue.toLowerCase().indexOf(filter) > -1) {
                    item.style.display = "";
                    hasVisibleItems = true;
                    hasVisibleItemsOverall = true;
                } else {
                    item.style.display = "none";
                }
            }
        }
        
        if (hasVisibleItems) {
            container.style.display = "";
            container.previousElementSibling.style.display = ""; // Show the heading
        } else {
            container.style.display = "none";
            container.previousElementSibling.style.display = "none"; // Hide the heading
        }
    }

    if (hasVisibleItemsOverall) {
        noResultsMessage.style.display = "none";
    } else {
        noResultsMessage.style.display = "block";
    }
}