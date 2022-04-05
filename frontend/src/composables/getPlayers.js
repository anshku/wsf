import axios from "axios";

const getPlayers = async () => {
  return await axios.get("http://localhost:8000/players");
};

export default getPlayers;
