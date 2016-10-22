using UnityEngine;
using System.Collections;

public class pingTest : MonoBehaviour
{

    public string url = "https://arc.applause.com/wp-content/uploads/2015/04/build_alex_kipman-1024x515.jpg";
    // Use this for initialization
    void Start () {
        
	}

    // Update is called once per frame
    void Update () {
	    
	}

    /*IEnumerator Start()
    {
        WWW www = new WWW(url);
        yield return www;
        Renderer renderer = GetComponent<Renderer>();
        renderer.material.mainTexture = www.texture;
    }*/
}
