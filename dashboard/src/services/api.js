import instance from ".";

export const getCountries = async () => {
  const { data } = await instance.get("/api/countries");
  return data.data;
};

export const getCategories = async () => {
  const { data } = await instance.get("/api/categories");
  return data.data;
};

export const getStartups = async (category, country) => {
  const { data } = await instance.get(`/api/startups/${category}/${country}`);
  return data.data;
};

export const getMedians = async (country) => {
  const { data } = await instance.get(`/api/median/${country}`);
  return data.data;
};
