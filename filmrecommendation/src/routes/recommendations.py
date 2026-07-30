from fastapi import APIRouter, HTTPException
from typing import List

from ..models.schemas import (
    RecommendationRequest, 
    RecommendationResponse, 
    FilmRecommendation,
    HealthResponse
)
from ..database.vector_store import vector_store_manager

router = APIRouter()


@router.get("/health", response_model=HealthResponse, summary="Health check endpoint")
async def health_check():
    """Health check endpoint to verify that the API is working"""
    return HealthResponse(message="Hello World")


@router.post(
    "/recommendations",
    response_model=RecommendationResponse,
    summary="Get similar film recommendations"
)
def get_recommendations(request: RecommendationRequest):
    """
    Find similar films based on a given description.
    
    Args:
        request: Request containing the film description and the desired number of recommendations
        
    Returns:
        List of recommended films with their titles and descriptions
        
    Raises:
        HTTPException: If validation fails or there is a database problem
    """
    if not vector_store_manager.vector_store:
        raise HTTPException(status_code=500, detail="The database is not connected")
    
    try:
        results = vector_store_manager.similarity_search(request.query, request.k)
        
        if not results:
            raise HTTPException(status_code=404, detail="No films found")
        
        # Convert to FilmRecommendation objects
        film_recommendations = [
            FilmRecommendation(
                title=result["title"], 
                description=result["description"],
                image_url=result.get("image_url", "")
            )
            for result in results
        ]
        
        return RecommendationResponse(results=film_recommendations)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
