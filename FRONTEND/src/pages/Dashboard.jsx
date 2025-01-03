import { useState } from "react"

export function Dashboard(){

    const months = ["Janvier", "Fevrirer", "Mars", "Avirl", "Mai", "Juin", "Juillet","Aout", "Septembre", "Octobre", "Novembre","Decembre"]

    //let date = new Date()
    let [date,setDate] = useState(new Date())
    let [day, setDay] = useState(date.getDate())
    let [month, setMonth] = useState(months[date.getMonth()])
    let newDate = date.setDate(15)
    let initialDay = 13 
    console.log(date)
    //console.log(typeof(date))
    //console.log(newDate.toLocaleString())

    /*const changeDate = (change)=>{
        if(change){
            //setDay(day+1)
            //setMonth(months[day]) 
            //initialDay=initialDay++
            date.setDate(day+1)
            setDay(day.getDate())
            console.log("Change Date")
        }
    }*/

    function changeDate(change){
        if(change){
            /*setDay(day+1)
            setMonth(months[day]) */
            //initialDay=initialDay++
            
            date.setDate(day+1)
            setDay(date.getDate())
            console.log(`Voici la nouvelle ${date}`)
            setMonth(months[date.getMonth()])
            console.log(date.getMonth())
           // console.log("Change Date")
        }
        else{
            date.setDate(day-1)
            setDay(date.getDate())
            console.log(`Voici la nouvelle ${date}`)
            setMonth(months[date.getMonth()])
            //console.log(date.getMonth())
        }
    }

    /*let tomorrow = day+1
    let futur = date.setDate(36)
    console.log(typeof(futur))
    console.log((futur+1).toLocaleString())
    //console.log(date)
    console.log(day)
    console.log(tomorrow)
    //console.log(tomorrow.toDateString())
    console.log(typeof(tomorrow))*/
    return (
        <div >
        <div className="flex">
        <div className="flex justify-start items-center h-screen w-[300px] bg-yellow-500">
            <div className="flex-column">
            <h1 className="text-9xl ">{day}</h1>
            <h2 className="text-5xl">{month}</h2>
            <div className="">
                <button className="h-[40px] w-[40px] bg-gray-300" onClick={()=>{changeDate(true)}}>+</button>
                <button className="h-[40px] w-[40px] bg-gray-500" onClick={()=>{changeDate(false)}}>-</button>
            </div>
            </div>
        </div>
        <div className="flex justify-center items-center h-[654px] w-[20px] bg-orange-500"></div>
        
        </div>
    </div>
    )
    
}