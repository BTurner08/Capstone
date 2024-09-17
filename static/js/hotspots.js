
function startBook() {

    // remove the button
    $('#btn-start').remove();

    // remove the center class
    $("#flipbook").removeClass("center-book");

    // flip the book
    setTimeout(() => {
        $("#flipbook").turn('next')
    }, 300);
}

function initBook() {
    $("#flipbook").turn({
        height: 780,
        autoCenter: true,
        page: 1,
        gradients: true,
        duration: 1000,
    });
}

function init() {

    console.log("Hotspots page");

    initBook();

    $('#btn-start').click(startBook);
}


window.onload = init;