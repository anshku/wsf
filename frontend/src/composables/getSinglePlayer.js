import axios from "axios";

const getSinglePlayers = async (id) => {
  return await axios.get("http://localhost:8000/players/" + id);
};

export default getSinglePlayers;
