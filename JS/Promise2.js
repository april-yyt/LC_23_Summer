const userLeft=false
const userWatchingCatMeme=true

// function wacthTutorialCallback(callback,errorCallback){
//     if (userLeft){
//         errorCallback({
//             name:'User Left',
//             message: ':('
//         })
//     } else if (userWatchingCatMeme){
//         errorCallback({
//             name:'User Watching Cat Meme',
//             message: 'WebDevSimplified < Cat'
//         })
//     } else{
//         callback('Thumns up and Subscribe')
//     }
// }

// wacthTutorialCallback((message)=>{
//     console.log('Success:'+message)
// }, (error)=>{
//     console.log(error.name + ' ' + error.message)
// })

function wacthTutorialPromise(){
    return new Promise((resolve,reject)=>{
        if (userLeft){
            errorCallback({
                name:'User Left',
                message: ':('
            })
        } else if (userWatchingCatMeme){
            errorCallback({
                name:'User Watching Cat Meme',
                message: 'WebDevSimplified < Cat'
            })
        } else{
            callback('Thumns up and Subscribe')
        }
    })
}

wacthTutorialPromise.then((message)=>{
    console.log('Success:'+message)
}).catch((error)=>{
    console.log(error.name + ' ' + error.message)
})