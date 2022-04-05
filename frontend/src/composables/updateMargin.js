import axios from "axios";

const updateMargin = async (id, margin) => {
  return await axios.patch("http://localhost:8000/players/" + id + "/", {
    margin,
  });
};

export default updateMargin;
