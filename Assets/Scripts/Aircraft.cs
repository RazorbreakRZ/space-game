using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Aircraft : MonoBehaviour {

    float engineForce = 10f;
    float rotationForce = -100f;
    float driftFactor = 1f;

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
        if (Input.GetButton("Acceleration"))
            rb.AddForce(transform.up * engineForce);
        rb.angularVelocity = Input.GetAxis("Rotation") * rotationForce;
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
