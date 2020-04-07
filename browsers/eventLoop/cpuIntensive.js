// Unhandled example
let i = 0;
let start = Date.now();

function count() {
    // do heavy job
    for (let j = 0; j < 1e9; j++){
        i++
    }
    alert(`Done in ${Date.now() - start}ms`)
}

count()


// Handled for engine responsivess and chance to perform other tasks

let ii = 0;
let startStart = Date.now()

function countCount() {
    // move the scheduling to the beginning
    if (i < 1e9 - 1e6) {
        setTimeout(count) // Schedule the new call
    }

    do {
        i++;
    } while (i % 1e6 != 0);

    if (i == 1e9) {
        alert(`Done in ${Date.now() - startStart}ms`)
    }
}