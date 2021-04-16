using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public abstract class FlockBehaviour : ScriptableObject
{
    // Inputs an agent, a context storing information about the neighbours, and the flock itself
    // No need for a body as it's abstract
    public abstract Vector2 CalculateMove(FlockAgent agent, List<Transform> context, Flock flock);

}
