using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// Use the physics system to check whether there is anything around us
[RequireComponent(typeof(Collider2D))]
public class FlockAgent : MonoBehaviour {

    Flock agentFlock;
    public Flock AgentFlock { get { return agentFlock; } }

    Collider2D agentCollider;
    // Public accessor for agentCollider, we only want to assign to it in the startup
    public Collider2D AgentCollider { get { return agentCollider; } }

    // Use this for initialization
    void Start()
    {
        agentCollider = GetComponent<Collider2D>();
    }

    public void Initialize(Flock flock)
    {
        agentFlock = flock; 
    }

    public void Move(Vector2 velocity)
    {
        transform.up = velocity;
        transform.position += (Vector3)velocity * Time.deltaTime;
    }


}
