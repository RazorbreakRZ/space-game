using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Aircraft : MonoBehaviour {

    float engineForce = 3f;
    float rotationForce = -150f;
    float driftFactor = 0f;

    // Use this for initialization
    void Start () {

	}
	
	// Update is called once per frame
	void Update () {
        
    }

    private void FixedUpdate()
    {
        Rigidbody2D rb = GetComponent<Rigidbody2D>();
        rb.velocity = ForwardVelocity() + RightVelocity() * driftFactor;
        //if (Input.GetButton("Acceleration"))
        rb.AddForce(transform.up * engineForce);
        rb.angularVelocity = Input.GetAxis("Rotation") * rotationForce;
        Debug.Log(rb.velocity.normalized);
        Debug.Log(rb.angularVelocity);
    }

    Vector2 ForwardVelocity()
    {
        return transform.up * Vector2.Dot(GetComponent<Rigidbody2D>().velocity, transform.up);
    }

    Vector2 RightVelocity()
    {
        return transform.right * Vector2.Dot(GetComponent<Rigidbody2D>().velocity, transform.right);
    }
}
