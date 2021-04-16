using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

// Add an attribute
[CustomEditor(typeof(CompositeBehavior))]
// Inherits from Editor
// Whenever we have a composite behaviour scriptable object, this tells how it should be rendered
public class CompositeBehaviorEditor : Editor {

    public override void OnInspectorGUI()
    {
        // Create reference to Composite Behavior
        CompositeBehavior cb = (CompositeBehavior)target;

        // Returns a rect where the cursor is (width, initial position of the cursor)
        Rect r = EditorGUILayout.BeginHorizontal();
        r.height = EditorGUIUtility.singleLineHeight;

        // Check for behaviors
        if (cb.behaviours == null || cb.behaviours.Length == 0)
        {
            EditorGUILayout.HelpBox("No behaviours in array", MessageType.Warning);
            EditorGUILayout.EndHorizontal();
            r = EditorGUILayout.BeginHorizontal();
            r.height = EditorGUIUtility.singleLineHeight;
        }
        else
        {
            // Set cursor to have a padding
            r.x = 30f;
            r.width = EditorGUIUtility.currentViewWidth - 95f;
            EditorGUI.LabelField(r, "Behaviours");
            r.x = EditorGUIUtility.currentViewWidth - 65f;
            r.width = 60f;
            EditorGUI.LabelField(r, "Weights");
            r.y += EditorGUIUtility.singleLineHeight * 1.2f;

            // If we change the behaviours, this gets triggered
            EditorGUI.BeginChangeCheck();
            for (int i = 0; i < cb.behaviours.Length; i++)
            {
                r.x = 5f;
                r.width = 20f;
                EditorGUI.LabelField(r, i.ToString());
                r.x = 30f;
                r.width = EditorGUIUtility.currentViewWidth - 95f;
                // Dropping in a behaviours
                cb.behaviours[i] = (FlockBehaviour)EditorGUI.ObjectField(r, cb.behaviours[i], typeof(FlockBehaviour), false);
                r.x = EditorGUIUtility.currentViewWidth - 65f;
                r.width = 60f;
                cb.weights[i] = EditorGUI.FloatField(r, cb.weights[i]);
                r.y += EditorGUIUtility.singleLineHeight * 1.1f;

            }
            if (EditorGUI.EndChangeCheck())
            {
                EditorUtility.SetDirty(cb);
            }
        }

        EditorGUILayout.EndHorizontal();
        r.x = 5f;
        r.width = EditorGUIUtility.currentViewWidth - 10f;
        r.y += EditorGUIUtility.singleLineHeight * 0.5f;

        if (GUI.Button(r, "Add Behaviour"))
        {
            // add behaviour
            AddBehaviour(cb);
            EditorUtility.SetDirty(cb);
        }

        r.y += EditorGUIUtility.singleLineHeight * 1.5f;
        // Only if there are behaviour to remove
        if (cb.behaviours != null && cb.behaviours.Length > 0)
        {
            if (GUI.Button(r, "Remove Behaviour"))
            {
                // remove behaviour
                RemoveBehaviour(cb);
                EditorUtility.SetDirty(cb);
            }
        }

    }

    void AddBehaviour(CompositeBehavior cb)
    {
        // Get the original size of the array
        int oldCount = (cb.behaviours != null) ? cb.behaviours.Length : 0;
        FlockBehaviour[] newBehaviours = new FlockBehaviour[oldCount + 1];
        float[] newWeights = new float[oldCount + 1];
        for (int i = 0; i < oldCount; i++)
        {
            newBehaviours[i] = cb.behaviours[i];
            newWeights[i] = cb.weights[i];
        }
        newWeights[oldCount] = 1f;
        cb.behaviours = newBehaviours;
        cb.weights = newWeights;
    }


    void RemoveBehaviour(CompositeBehavior cb)
    {
        // Get the original size of the array
        int oldCount = cb.behaviours.Length;
        if (oldCount == 1)
        {
            cb.behaviours = null;
            cb.weights = null;
            return;
        }
        FlockBehaviour[] newBehaviours = new FlockBehaviour[oldCount - 1];
        float[] newWeights = new float[oldCount - 1];
        for (int i = 0; i < oldCount-1; i++)
        {
            newBehaviours[i] = cb.behaviours[i];
            newWeights[i] = cb.weights[i];
        }
        cb.behaviours = newBehaviours;
        cb.weights = newWeights;
    }
}
