import { useState, useEffect } from "react"

function Home() {

    const[status, setStatus] = useState<string>("chargement...")

    useEffect(()=>{
        fetch("http://127.0.0.1:8000/api/health")
            .then((reponse) =>  reponse.json()) 
            .then((donnee) => setStatus(donnee.status))
            .catch(()=> setStatus("erreur"))
    }, []);
    return (
        <main>
            <p>{status}</p>
        </main>
    )
}

export default Home;