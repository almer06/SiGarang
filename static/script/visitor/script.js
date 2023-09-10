window.addEventListener('beforeunload', () => {
    document.getElementById('load-page').classList.add('d-flex')
    console.log('loading...')
})

window.addEventListener('DOMContentLoaded', () => {
    document.getElementById('load-page').classList.add('d-none')
    console.log('done')
})
