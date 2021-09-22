import React from "react";
import Info from "./components/info";
import Form from "./components/form";
import WeatheAutt from "./components/weathe _autt";
import HurlyWeather from "./components/HurlyWeather";

const API_key = "0ba9122c7db41155430fb755e75d71e0";
const London_API = `https://api.openweathermap.org/data/2.5/onecall?lat=51.30&lon=0.07&appid=${API_key}&lang=ru&units=metric`;
const Moscow_API = `https://api.openweathermap.org/data/2.5/onecall?lat=55.45&lon=37.36&appid=${API_key}&lang=ru&units=metric`;
const Madrid_API = `https://api.openweathermap.org/data/2.5/onecall?lat=50.27&lon=30.31&appid=${API_key}&lang=ru&units=metric`;
const Minsk_API = `https://api.openweathermap.org/data/2.5/onecall?lat=52.13&lon=21.00&appid=${API_key}&lang=ru&units=metric`;



class App extends React.Component {
  state={
    api:undefined,
    ex:undefined,
    temp:undefined,
    city:undefined,
    pressure: undefined,
    error:undefined

  }

  //getPosition = ()=>{
  //  navigator.geolocation.getCurrentPosition((pos)=>{
  //     const lat= pos.coords.latitude
  //     const lon= pos.coords.longitude
  //     console.log(lat,lon)
  //     
  //  })
//}
  gettingweather = async(e)=>{
    e.preventDefault();
    const exclude = e.target.elements.exclude.value;
    const city = e.target.elements.city.value;
   

    //if(exclude === "current"){
    if(city === "London"){
    const api_url = await
    fetch(London_API)
    const date = await api_url.json()
    console.log(date)

  
    this.setState({
      api:date,
      ex:exclude,
      temp:date.current.temp,
      city:date.timezone,
      pressure:date.current.pressure,
      error:""


    })

  }
  if(city === "Moscow"){
    const api_url = await
    fetch(Moscow_API)
    const date = await api_url.json()
    console.log(date)

  
    this.setState({
      api:date,
      temp:date.current.temp,
      city:date.timezone,
      pressure:date.current.pressure,
      error:""


    })
  }
  if(city === "Madrid"){
    const api_url = await
    fetch(Madrid_API)
    const date = await api_url.json()
    console.log(date)

  
    this.setState({
      api:date,
      temp:date.current.temp,
      city:date.timezone,
      pressure:date.current.pressure,
      error:""


    })
  }
  if(city === "Minsk"){
    const api_url = await
    fetch(Minsk_API)
    const date = await api_url.json()
    console.log(date)

  
    this.setState({
      api:date,
      temp:date.current.temp,
      city:date.timezone,
      pressure:date.current.pressure,
      error:""


    })
  }
  

//}
  }
  render(){
    return(
      <div className="container">
        <Form 
        weatherMetod = {this.gettingweather}/>

        <Info/>
        
        <WeatheAutt
        temp={this.state.temp}
        city={this.state.city}
        pressure={this.state.pressure}
        error  = {this.state.error}
        api = {this.state.api}
        />
        <HurlyWeather api = {this.state.api}
         exclude = {this.state.ex}/>
      </div>

      

    );
  }
}

export default App