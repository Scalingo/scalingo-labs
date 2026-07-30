from pydantic import BaseModel, Field
from typing import List, Optional


class RecommendationRequest(BaseModel):
    """Model for film recommendation requests"""
    query: str = Field(
        ...,
        min_length=10,
        description="Description of the film being searched for (minimum 10 characters)"
    )
    k: int = Field(
        default=3,
        ge=1,
        le=5,
        description="Number of recommendations (between 1 and 5)"
    )


class FilmRecommendation(BaseModel):
    """Model for a film recommendation"""
    title: str = Field(..., description="Film title")
    description: str = Field(..., description="Film description")
    image_url: Optional[str] = Field(None, description="URL of the film poster")


class RecommendationResponse(BaseModel):
    """Model for the recommendation response"""
    results: List[FilmRecommendation] = Field(..., description="List of recommended films")


class HealthResponse(BaseModel):
    """Model for the API health response"""
    message: str = Field(..., description="Status message")
