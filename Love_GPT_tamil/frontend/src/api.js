export const generateLovePlan = async (story) => {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/generate_love_plan", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ story }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || "Something went wrong generating the plan.");
    }

    const data = await response.json();
    return data.plan;
  } catch (error) {
    console.error("API Error:", error);
    throw error;
  }
};
