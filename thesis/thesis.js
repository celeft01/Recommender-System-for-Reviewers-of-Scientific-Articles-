
class Data {
    constructor(name, /*k1, k2*/k, eN, e, ca, initialI){
        this.name = name;
        // this.keyword1score = k1;
        // this.keyword2score = k2;
        this.keywordscores=k;
        this.entriesN = eN;
        this.entries=e;
        this.coauthor=ca;
        this.inI=initialI;

        let sum=0;
        for(let i=0; i<k.length; i++){
            sum=sum+k[i][0];
        }

        this.keySum=sum;
    }
    
    
}

document.getElementById("btn4").addEventListener("click", function(){clearF()});

var clearB=false;

function clearF(){
    console.log("in clear function");
    clearB=true;

    if(counter!==0){
        clearTable();
    }


    document.getElementById("fullname").value="";
    document.getElementById("key1").value="";
    // document.getElementById("key2").value="";
    document.getElementById("resnum").value="";

}




function clearTable(){
    let table = document.getElementById("tbl1");
    console.log(document.getElementById("resnum").value);
    for(let i=0; i<document.getElementById("resnum").value; i++){
        table.deleteRow(1);
    }
}
    
var counter=0;

function sortResultTable(col){

    let table = document.getElementById("tbl1");
    for(let i=0; i<document.getElementById("resnum").value; i++){
        table.deleteRow(1);
    }

    if(col==='kwords'){
        var sortedT=resultTable.sort(function (a , b){
            return (b.keySum)-(a.keySum);
        });
        createTable(sortedT);
    }
    else{
        var sortedT=resultTable.sort(function (a , b){
            return b.entriesN-a.entriesN;
        });
        createTable(sortedT);
    }

}




function createTable(resultsTable){
    
    


    
    let table = document.getElementById("tbl1");

    for(let i=0; i< document.getElementById("resnum").value; i++){
        let row = table.insertRow(-1);
                    
                        // Create table cells
        let c1 = row.insertCell(0);
        let c2 = row.insertCell(1);
        let c3 = row.insertCell(2);
        let c4=row.insertCell(3);
        c1.innerText = resultsTable[i].name;

        

        var b =document.createElement("button");
        b.id="button"+i;
        b.classList.add("btn");
        b.classList.add("btn-primary");
        b.setAttribute("data-bs-toggle", "modal");
        b.setAttribute("data-bs-target", "#modal1");
        // b.innerText="Keyword 1 score: "+resultsTable[i].keyword1score+" Keyword 2 score: "+resultsTable[i].keyword2score;
        let text12="";

        for(let j=0; j<resultsTable[i].keywordscores.length; j++){
            text12=text12+resultsTable[i].keywordscores[j][1]+" : "+resultsTable[i].keywordscores[j][0]+"\n";
        }
        b.innerText=text12;


        b.addEventListener("click", function(){modalf(resultsTable[i].inI)});

        c2.append(b);


        entriestext="";
        for(let k=0; k<resultsTable[i].entries.length; k++){
            entriestext=entriestext+resultsTable[i].entries[k]+"\n";
        }
        c3.innerText = entriestext;
        c4.innerText=resultsTable[i].coauthor;
        

        
    }

}








function modalf(i){
    console.log("in modal function")

    
    textModal="";
    for(let j=0; j<myR[2][i].length; j++){
        textModal=textModal+myR[2][i][j][1].bold()+" ("+myR[2][i][j][0]+") : <br>";
        // "+myR[2][i][j]+" \n";
        for (let k=2; k<myR[2][i][j].length; k++){
            textModal=textModal+"-"+myR[2][i][j][k]+"<br>";
        }
    }
    // document.getElementById("modalbody").innerText="Keyword 1:\n"+myR[2][i][0]+"\nKeyword 2:\n"+myR[2][i][1];

    document.getElementById("modalbody").innerHTML=textModal;
}






function cValid(str){
    if(str[str.length-1]==","){
        return false;
    }
    for (let i = 0; i < str.length; i++) {
        if(str[i]===','){
            if(str[i-1]===" " && str[i+1]===" "){
                
                if(/[^a-zA-Z0-9]/.test(str[i-2]) || /[^a-zA-Z0-9]/.test(str[i+2])){
                    return false;
                }

            }
            else{
                return false;
            }
        }
    }

    return true;
}


function checkInput(){
    var b1=0;
    var b2=0;
    var b3=0;
    var b4=0;
    if(document.getElementById("fullname").value.trim().length===0 || !cValid(document.getElementById("fullname").value)){
        b1=1;
        document.getElementById("c1").classList.remove("d-none");
    }else{
        document.getElementById("c1").classList.add("d-none");
    }
    if(document.getElementById("key1").value.trim().length===0 || !cValid(document.getElementById("key1").value)){
        b2=1;
        document.getElementById("c2").classList.remove("d-none");
    }else{
        document.getElementById("c2").classList.add("d-none");
    }
    // if(document.getElementById("key2").value.trim().length===0){
    //     b3=1;
    //     document.getElementById("c3").classList.remove("d-none");
    // }else{
    //     document.getElementById("c3").classList.add("d-none");
    // }
    if(document.getElementById("resnum").value.trim().length===0 ||isNaN(document.getElementById("resnum").value) || (document.getElementById("resnum").value<1 || document.getElementById("resnum").value>100)){
        b4=1;
        document.getElementById("c4").classList.remove("d-none");
    }else{
        document.getElementById("c4").classList.add("d-none");
    }

    if(b1===1 || b2===1 || b3===1 || b4===1){
        return false;
    }
    else{
        return true;
    }
}


var myR;

var resultTable=[];

function booktitles(){

    // document.getElementById("results").innerHTML="working on it...";
    if(checkInput()){


        
        document.getElementById("c1").classList.add("d-none");
        document.getElementById("c2").classList.add("d-none");
        // document.getElementById("c3").classList.add("d-none");
        document.getElementById("c4").classList.add("d-none");


        var displaynum=document.getElementById("resnum").value;

        document.getElementById("btn1").disabled=true;

        
        var fname=document.getElementById("fullname").value;

        

        var key1=document.getElementById("key1").value;
        // var key2=document.getElementById("key2").value;

        const xhr=new XMLHttpRequest();


        // Setup our listener to process completed requests
        xhr.onreadystatechange = function () {
            // Only run if the request is complete
            if (xhr.readyState !== 4) return;
            // Process our return data
            if (xhr.status >= 200 && xhr.status < 300) {
                // console.log(xhr.responseText)
                myR=JSON.parse(xhr.responseText);
                // console.log(myR[1]);
                console.log(myR[5]);
                var data={};

                for(let i=0; i<displaynum; i++){




                    // resultTable.push(new Data(myR[0][i], myR[2][i][0][0], myR[2][i][1][0], myR[3][i].length, myR[3][i], myR[4][i], i));
                    resultTable.push(new Data(myR[0][i], myR[2][i], myR[3][i].length, myR[3][i], myR[4][i], i));

                    

                
                }

                if(counter!==0){
                    if(clearB===true){
                        clearB=false;
                    }
                    else{
                        clearTable();
                    }
                }
                console.log(resultTable);
                createTable(resultTable);
                counter=counter+1;
                
                //

            } else {
                console.log('error', xhr);
            }
        };


        xhr.onload=function(){

            
            document.getElementById("btn1").disabled=false;
        }

        xhr.open('POST', 'thesis.php');
        xhr.setRequestHeader("Content-type", "application/json");

        
        

        
        const data={};
        data.function='booktitles';
        data.fullname=document.getElementById("fullname").value;
        data.key1=document.getElementById("key1").value;
        // data.key2=document.getElementById("key2").value;



        xhr.send(JSON.stringify(data));
    }
    

    
    

}



function journals(){

    // document.getElementById("results").innerHTML="working on it...";
    if(checkInput()){

        
        document.getElementById("c1").classList.add("d-none");
        document.getElementById("c2").classList.add("d-none");
        // document.getElementById("c3").classList.add("d-none");
        document.getElementById("c4").classList.add("d-none");


        var displaynum=document.getElementById("resnum").value;

        document.getElementById("btn2").disabled=true;

        var fname=document.getElementById("fullname").value;
        var key1=document.getElementById("key1").value;
        // var key2=document.getElementById("key2").value;

        const xhr=new XMLHttpRequest();


        // Setup our listener to process completed requests
        xhr.onreadystatechange = function () {
            // Only run if the request is complete
            if (xhr.readyState !== 4) return;
            // Process our return data
            if (xhr.status >= 200 && xhr.status < 300) {
                myR=JSON.parse(xhr.responseText);
                console.log(myR[5]);
                // console.log(myR[1]);

                for(let i=0; i<displaynum; i++){




                    // resultTable.push(new Data(myR[0][i], myR[2][i][0][0], myR[2][i][1][0], myR[3][i].length, myR[3][i], myR[4][i], i));
                    resultTable.push(new Data(myR[0][i], myR[2][i], myR[3][i].length, myR[3][i], myR[4][i], i));

                    

                
                }

                if(counter!==0){
                    if(clearB===true){
                        clearB=false;
                    }
                    else{
                        clearTable();
                    }
                }
                console.log(resultTable);
                createTable(resultTable);
                counter=counter+1;
                
                //

            } else {
                console.log('error', xhr);
            }
        };


        xhr.onload=function(){
            // document.getElementById("results").innerHTML=this.responseText;
            document.getElementById("btn2").disabled=false;
        }

        xhr.open('POST', 'thesis.php');
        xhr.setRequestHeader("Content-type", "application/json");

        
        

        const data={};
        data.function='journals';
        data.fullname=document.getElementById("fullname").value;
        data.key1=document.getElementById("key1").value;
        // data.key2=document.getElementById("key2").value;



        xhr.send(JSON.stringify(data));
    }

    
    

}



// function booktitlesANDjournals(){

//     // document.getElementById("results").innerHTML="working on it...";
//     if(checkInput()){

        
//         document.getElementById("c1").classList.add("d-none");
//         document.getElementById("c2").classList.add("d-none");
//         // document.getElementById("c3").classList.add("d-none");
//         document.getElementById("c4").classList.add("d-none");


//         var displaynum=document.getElementById("resnum").value;

//         document.getElementById("btn3").disabled=true;

//         var fname=document.getElementById("fullname").value;
//         var key1=document.getElementById("key1").value;
//         // var key2=document.getElementById("key2").value;

//         const xhr=new XMLHttpRequest();


//         // Setup our listener to process completed requests
//         xhr.onreadystatechange = function () {
//             // Only run if the request is complete
//             if (xhr.readyState !== 4) return;
//             // Process our return data
//             if (xhr.status >= 200 && xhr.status < 300) {
//                 myR=JSON.parse(xhr.responseText);
                

//                 for(let i=0; i<displaynum; i++){




//                     // resultTable.push(new Data(myR[0][i], myR[2][i][0][0], myR[2][i][1][0], myR[3][i].length, myR[3][i], myR[4][i], i));
//                     resultTable.push(new Data(myR[0][i], myR[2][i], myR[3][i].length, myR[3][i], myR[4][i], i));

                    

                
//                 }

//                 if(counter!==0){
//                     clearTable();
//                 }
//                 console.log(resultTable);
//                 createTable(resultTable);
//                 counter=counter+1;

//             } else {
//                 console.log('error', xhr);
//             }
//         };


//         xhr.onload=function(){
//             // document.getElementById("results").innerHTML=this.responseText;
//             document.getElementById("btn3").disabled=false;
//         }

//         xhr.open('POST', 'thesis.php');
//         xhr.setRequestHeader("Content-type", "application/json");

        
        

//         const data={};
//         data.function='booktitlesANDjournals'
//         data.fullname=document.getElementById("fullname").value;
//         data.key1=document.getElementById("key1").value;
//         // data.key2=document.getElementById("key2").value;



//         xhr.send(JSON.stringify(data));
//     }

    
    

// }



function booktitlesANDjournals(){

    // document.getElementById("results").innerHTML="working on it...";
    if(checkInput()){


        
        document.getElementById("c1").classList.add("d-none");
        document.getElementById("c2").classList.add("d-none");
        // document.getElementById("c3").classList.add("d-none");
        document.getElementById("c4").classList.add("d-none");


        var displaynum=document.getElementById("resnum").value;

        document.getElementById("btn3").disabled=true;

        
        var fname=document.getElementById("fullname").value;

        

        var key1=document.getElementById("key1").value;
        // var key2=document.getElementById("key2").value;

        const xhr=new XMLHttpRequest();


        // Setup our listener to process completed requests
        xhr.onreadystatechange = function () {
            // Only run if the request is complete
            if (xhr.readyState !== 4) return;
            // Process our return data
            if (xhr.status >= 200 && xhr.status < 300) {
                console.log(xhr.responseText);
                // myR=JSON.parse(xhr.responseText);
                myR=JSON.parse(xhr.responseText);
                console.log(myR[5]);
                

                var data={};

                for(let i=0; i<displaynum; i++){




                    // resultTable.push(new Data(myR[0][i], myR[2][i][0][0], myR[2][i][1][0], myR[3][i].length, myR[3][i], myR[4][i], i));
                    resultTable.push(new Data(myR[0][i], myR[2][i], myR[3][i].length, myR[3][i], myR[4][i], i));

                    

                
                }

                if(counter!==0){
                    if(clearB===true){
                        clearB=false;
                    }
                    else{
                        clearTable();
                    }
                }
                console.log(resultTable);
                createTable(resultTable);
                counter=counter+1;
                
                //

            } else {
                console.log('error', xhr);
            }
        };


        xhr.onload=function(){

            
            document.getElementById("btn3").disabled=false;
        }

        xhr.open('POST', 'thesis.php');
        xhr.setRequestHeader("Content-type", "application/json");

        
        

        
        const data={};
        data.function='booktitlesANDjournals';
        data.fullname=document.getElementById("fullname").value;
        data.key1=document.getElementById("key1").value;
        // data.key2=document.getElementById("key2").value;



        xhr.send(JSON.stringify(data));
    }
    

    
    

}








var button1=document.getElementById("btn1");
button1.addEventListener("click", function () { booktitles() });

var button2=document.getElementById("btn2");
button2.addEventListener("click", function () { journals() });

var button3=document.getElementById("btn3");
button3.addEventListener("click", function () { booktitlesANDjournals() });





